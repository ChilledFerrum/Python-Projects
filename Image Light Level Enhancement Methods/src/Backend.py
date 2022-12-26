import os
import os.path

# Change this to True if you do not want Progress Bar visuals, otherwise > pip install curses
disableProgressBar = False

if not disableProgressBar:
    try:
        import curses
    except ImportError:
        print("\033[91mModuleNotFoundError: No module named 'curses'\033[92m\n"
              "This module is primarily for visuals and can be disabled\n"
              "Enable if you need the Progress Bar visuals\n"
              "\nPossible Solutions:\033[0m\n"
              "  > Disable Progress Bar in src/Backend.py\n"
              "  > pip install curses")
        exit(-1)

try:
    import cv2 as cv
except ImportError:
    print("ModuleNotFoundError: No module named 'cv2'\n"
          "Please Install OpenCV to your Python environment")
    exit(-1)

barChar = "█"

bufferedString = ""
total = 0

def setMaxLimit(max):
    global total
    total = max


def progressBar(current, stdScr):
    try:
        completed = 100 * (current / float(total))
    except ZeroDivisionError:
        completed = 0
    barProgress = barChar * int(completed) + "-" * (100 - int(completed))

    stdScr.addstr(0, 117, f"| {completed:.0f} %")
    curses.init_pair(1, 22, -1)
    stdScr.addstr(0, 0, f"Total Progress: |")
    stdScr.addstr(0, 17, f"{barProgress}", curses.color_pair(1))
    stdScr.addstr(1, 0, bufferedString)
    stdScr.refresh()
    if completed >= 100.0:
        print(f"Total Progress: |\033[92m{barProgress}\033[0m| {completed:.0f} %")

class Backend:
    def __init__(self):
        if not disableProgressBar:
            self.stdScr = curses.initscr()
            curses.noecho()
            curses.nocbreak()

        self.imagesBuffer = []
        self.imageName = []
        self.pathInput = ""
        self.pathOutput = ""
        self.outputTemplate = "/"

        self.numFiles = 0
        self.numProcesses = 0
        self.currentProcess = 0

        self.files = []


    def verify(self):
        if not disableProgressBar:
            global bufferedString
            bufferedString = "Verifying Files...\n"
            self.numFiles = len(self.files)
            self.numProcesses = self.numFiles + self.numFiles * 2
            setMaxLimit(self.numProcesses)

            progressBar(0, self.stdScr)

        for i, file in enumerate(self.files):
            if not (file.endswith(".png")) and not (file.endswith(".jpg")) and not (file.endswith(".JPG")) and not \
                    (file.endswith(".JPEG")) and not (file.endswith(".jpeg")):
                print("Reading incorrect or unsupported file formats. Supported file formats (jpg, jpeg, png")
                print("ERROR AT FILE:", file)
                exit(-1)
            if file.endswith(".png") or file.endswith(".PNG"):
                os.rename(os.path.join(self.pathInput, file), os.path.join(self.pathInput, ''.join([file])))
            elif file.endswith(".jpg") or file.endswith(".JPG"):
                os.rename(os.path.join(self.pathInput, file), os.path.join(self.pathInput, ''.join([file])))
            elif file.endswith(".JPEG"):
                os.rename(os.path.join(self.pathInput, file), os.path.join(self.pathInput, ''.join([file])))
            self.currentProcess += 1
            if not disableProgressBar:
                progressBar(self.currentProcess, self.stdScr)


    def readingImages(self):
        if not disableProgressBar:
            global bufferedString
            bufferedString = "Reading Images...\n"
            # sys.stdin.flush()
            progressBar(self.currentProcess, self.stdScr)
        for i, file in enumerate(self.files):
            if i == self.numFiles:
                return

            name = "/" + file
            img = cv.imread(self.pathInput + name)

            self.imagesBuffer.append(img)
            self.imageName.append(name)
            if not disableProgressBar:
                self.currentProcess += 1
                progressBar(self.currentProcess, self.stdScr)
        if not disableProgressBar:
            bufferedString = "Applying Filter..."


    def writeImages(self, index, img, file):
        if file.endswith(".png") or file.endswith(".PNG"):
            cv.imwrite(self.pathOutput + file, img)
        elif file.endswith(".jpg") or file.endswith(".JPG"):
            cv.imwrite(self.pathOutput + file, img)
        elif file.endswith(".JPEG"):
            cv.imwrite(self.pathOutput + file, img)
        if not disableProgressBar:
            self.currentProcess += 1
            progressBar(self.currentProcess, self.stdScr)
        return


    def run(self):
        if not (os.path.exists(self.pathInput)) or not os.path.exists(self.pathOutput):
            print("Input or Output Path does not Exist")
            exit(-1)

        self.files = os.listdir(self.pathInput)

        if not disableProgressBar:
            curses.start_color()
            curses.use_default_colors()
        self.verify()
        self.readingImages()


    def setInputPath(self, input):
        self.pathInput = input


    def setOutPath(self, input):
        self.pathOutput = input
