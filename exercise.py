from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
import logging
import sys,time
import cv2
import easydict
from homefit.tf_pose.networks import get_graph_path, model_wh
from homefit.tf_pose.estimator import TfPoseEstimator
from pygame import mixer

class Example(object):
    def __init__(self):
        self.flag = 0

    def setupUi(self, MainWindow,case):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1280, 720)
        MainWindow.setStyleSheet("background-color:rgb(255,255,255)\n")

        self.frame = QLabel(MainWindow)
        self.frame.setScaledContents(True)
        self.frame.move(5, 5)

        self.youframe = QLabel(MainWindow)
        self.youframe.setScaledContents(True)
        self.youframe.move(5, 5)

        self.btn_off = QPushButton("끄기", MainWindow)
        self.btn_off.resize(100, 25)
        self.btn_off.clicked.connect(self.stop)

        self.time = QTime(0, 0, 0)
        self.label = QLabel("시간 : ")
        self.label2 = QLabel("자세 : ")

        framelayout = QVBoxLayout()
        framelayout.addWidget(self.frame, 95)
        framelayout.addWidget(self.label, 5)

        youframelayout = QVBoxLayout()
        youframelayout.addWidget(self.youframe, 95)
        youframelayout.addWidget(self.btn_off, 5)
        youframelayout.addWidget(self.label2, 5)

        layout = QHBoxLayout()
        layout.addLayout(framelayout)
        layout.addLayout(youframelayout)

        MainWindow.setLayout(layout)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.case = case
        self.course(self.case)

    def course(self, case):

        # self.file = 'homefit/exercise/0.wmv' + case
        self.file = 'homefit/exercise/0.wmv'

        if (case == 1):
            self.file = 'homefit/exercise/0.wmv'
        elif(case == 2):
            self.file = 'homefit/exercise/1.wmv'
        elif(case == 3):
            self.file = 'homefit/exercise/2.wmv'
        elif(case == 4):
            self.file = 'homefit/exercise/3.wmv'
        elif(case == 5):
            self.file = 'homefit/exercise/4.wmv'
        elif(case == 6):
            self.file = 'homefit/exercise/5.wmv'
        elif(case == 7):
            self.file = 'homefit/exercise/6.wmv'
        elif(case == 8):
            self.file = 'homefit/exercise/7.wmv'
        elif(case == 9):
            self.file = 'homefit/exercise/8.wmv'
        elif(case == 10):
            self.file = 'homefit/exercise/8.wmv'

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def timerEvent(self):
        self.time = QTime.addSecs(self.time, 1)
        self.label.setText("시간 : " + self.time.toString("hh:mm:ss"))

    def start(self):
        self.flag = 1
        self.btn_off.setText("끄기")
        self.timer = QTimer()
        self.timer.timeout.connect(self.timerEvent)
        self.timer.start(1000)

    def nextFrameSlot(self):
        logger = logging.getLogger('TfPoseEstimator-WebCam')
        logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        fps_time = 0
        mixer.init()

        args = easydict.EasyDict({
            "camera": 0,
            "resize": "432x368",
            "resize_out_ratio": 4.0,
            "model": 'mobilenet_thin',
            "show-process": False

        })

        logger.debug('initialization %s : %s' % (args.model, get_graph_path(args.model)))
        w, h = model_wh(args.resize)
        if w > 0 and h > 0:
            e = TfPoseEstimator(get_graph_path(args.model), target_size=(w, h))

        else:
            e = TfPoseEstimator(get_graph_path(args.model), target_size=(432, 368))
        logger.debug('cam read+')

        cam = cv2.VideoCapture(args.camera)
        vdo = cv2.VideoCapture(self.file)

        vdo.get(cv2.CAP_PROP_FPS)

        ret_val, image = cam.read()
        logger.info('cam image=%dx%d' % (image.shape[1], image.shape[0]))

        count = 0
        ready = False
        text = ""

        while True:
            ret_val, image = cam.read()
            ret_val2, image2 = vdo.read()

            image2 = image2[50:700, 400:900]

            humans = e.inference(image, resize_to_default=(w > 0 and h > 0), upsample_size=args.resize_out_ratio)
            image, count, ready, text = TfPoseEstimator.draw_humans(image, humans, self.case, count, ready, text,
                                                                        imgcopy=False)
            if (self.label2.text().split(':')[1][1:] != text):
                self.label2.setText("자세 : " + text)

                if(text[0]=='교'):
                    mixer.music.load('sound/'+str(self.case)+'-1.mp3')
                    mixer.music.play()
                # elif(ready==True):
                    # mixer.music.load('sound/'+str(self.case)+str(count)+'.mp3')
                    # mixer.music.play()
                elif(ready==False):
                    mixer.music.load('sound/'+str(self.case)+'0.mp3')
                    mixer.music.play()

            image = cv2.flip(image, 1)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image2 = cv2.flip(image2, 1)
            image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)

            cv2.putText(image,
                        "FPS: %f" % (1.0 / (time.time() - fps_time)),
                        (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                        (255, 255, 0), 2)

            cv2.putText(image,
                        "ready: %d" % (ready),
                        (300, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                        (255, 255, 0), 2)

            cv2.putText(image,
                        "count: %d" % (count),
                        (500, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                        (255, 255, 0), 2)

            fps_time = time.time()
            self.frame.setPixmap(QtGui.QPixmap.fromImage(QtGui.QImage(image, image.shape[1], image.shape[0],
                                                                        QtGui.QImage.Format_RGB888)))
            self.youframe.setPixmap(QtGui.QPixmap.fromImage(QtGui.QImage(image2, image2.shape[1], image2.shape[0],
                                                                        QtGui.QImage.Format_RGB888)))

            if cv2.waitKey(1) & 0xFF == ord('q') or self.flag == 0 or count==15:
                cam.release()
                vdo.release()
                self.stop()
                break

        cv2.destroyAllWindows()

    def stop(self):
        try:
            self.flag = 0
            self.frame.setPixmap(QPixmap.fromImage(QImage()))
            self.youframe.setPixmap(QPixmap.fromImage(QImage()))
            self.timer.stop()
            self.label.setText("시간 : ")
            self.label2.setText("자세 : ")
        except:
            self.btn_off.setText("켜기를 먼저 눌러주세요.")

    def closeEvent(self, event=None):
        MainWindow.close(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Example()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())