import sys
import random
import winsound

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(700, 700)
        Form.setMinimumSize(QtCore.QSize(700, 700))
        Form.setMaximumSize(QtCore.QSize(700, 700))
        self.horizontalWidget = QtWidgets.QWidget(Form)
        self.horizontalWidget.setGeometry(QtCore.QRect(10, 590, 671, 61))
        self.horizontalWidget.setMaximumSize(QtCore.QSize(900, 700))
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.sword = QtWidgets.QPushButton(self.horizontalWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.sword.setFont(font)
        self.sword.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("sword_image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sword.setIcon(icon)
        self.sword.setIconSize(QtCore.QSize(18, 18))
        self.sword.setObjectName("sword")
        self.horizontalLayout.addWidget(self.sword)

        self.shield = QtWidgets.QPushButton(self.horizontalWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.shield.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("shield_image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.shield.setIcon(icon1)
        self.shield.setIconSize(QtCore.QSize(18, 18))
        self.shield.setObjectName("shield")
        self.horizontalLayout.addWidget(self.shield)

        self.player_name = QtWidgets.QLabel(Form)
        self.player_name.setGeometry(QtCore.QRect(60, 280, 151, 31))
        self.player_name.setStyleSheet("font: 75 18pt \"Times New Roman\";")
        self.player_name.setObjectName("player_name")

        self.enemy_name = QtWidgets.QLabel(Form)
        self.enemy_name.setGeometry(QtCore.QRect(460, 280, 151, 31))
        self.enemy_name.setStyleSheet("font: 75 18pt \"Times New Roman\";")
        self.enemy_name.setObjectName("enemy_name")

        self.hp_text = QtWidgets.QLabel(Form)
        self.hp_text.setGeometry(QtCore.QRect(90, 310, 41, 31))
        self.hp_text.setStyleSheet("font: 75 18pt \"Times New Roman\";")
        self.hp_text.setObjectName("hp_text")

        self.player_hp = QtWidgets.QLabel(Form)
        self.player_hp.setGeometry(QtCore.QRect(130, 310, 41, 31))
        self.player_hp.setStyleSheet("font: 75 18pt \"Times New Roman\";")
        self.player_hp.setObjectName("player_hp")

        self.enemy_hp_text = QtWidgets.QLabel(Form)
        self.enemy_hp_text.setGeometry(QtCore.QRect(500, 310, 41, 31))
        self.enemy_hp_text.setStyleSheet("font: 75 18pt \"Times New Roman\";")
        self.enemy_hp_text.setObjectName("enemy_hp_text")

        self.enemy_hp = QtWidgets.QLabel(Form)
        self.enemy_hp.setGeometry(QtCore.QRect(540, 310, 41, 31))
        self.enemy_hp.setStyleSheet("font: 75 18pt \"Times New Roman\";")
        self.enemy_hp.setObjectName("enemy_hp")

        self.actions = QtWidgets.QLabel(Form)
        self.actions.setGeometry(QtCore.QRect(240, 340, 201, 41))
        self.actions.setStyleSheet("font: 75 18pt \"Times New Roman\";")
        self.actions.setObjectName("actions")

        self.actions_text = QtWidgets.QLabel(Form)
        self.actions_text.setGeometry(QtCore.QRect(50, 390, 591, 151))
        self.actions_text.setStyleSheet("font: 75 16pt \"Times New Roman\";")
        self.actions_text.setObjectName("actions_text")

        self.actions_2 = QtWidgets.QLabel(Form)
        self.actions_2.setGeometry(QtCore.QRect(220, 550, 241, 41))
        self.actions_2.setStyleSheet("font: 75 18pt \"Times New Roman\";")
        self.actions_2.setObjectName("actions_2")

        self.avatar1 = QtWidgets.QLabel(Form)
        self.avatar1.setGeometry(QtCore.QRect(20, 20, 250, 250))
        self.avatar1.setMinimumSize(QtCore.QSize(250, 250))
        self.avatar1.setMaximumSize(QtCore.QSize(250, 250))
        self.avatar1.setText("")
        self.avatar1.setPixmap(QtGui.QPixmap("avatar1.png"))
        self.avatar1.setScaledContents(True)
        self.avatar1.setObjectName("avatar1")

        self.avatar2 = QtWidgets.QLabel(Form)
        self.avatar2.setGeometry(QtCore.QRect(430, 20, 250, 250))
        self.avatar2.setMinimumSize(QtCore.QSize(250, 250))
        self.avatar2.setMaximumSize(QtCore.QSize(250, 250))
        self.avatar2.setText("")
        self.avatar2.setPixmap(QtGui.QPixmap("avatar2.png"))
        self.avatar2.setScaledContents(True)
        self.avatar2.setObjectName("avatar2")

        self.done = QtWidgets.QPushButton(Form)
        self.done.setGeometry(QtCore.QRect(250, 650, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.done.setFont(font)
        self.done.setObjectName("done")

        self.shield_exist1 = QtWidgets.QLabel(Form)
        self.shield_exist1.setGeometry(QtCore.QRect(190, 280, 51, 51))
        self.shield_exist1.setText("")
        self.shield_exist1.setPixmap(QtGui.QPixmap(""))
        self.shield_exist1.setScaledContents(True)
        self.shield_exist1.setObjectName("shield_exist1")

        self.shield_exist2 = QtWidgets.QLabel(Form)
        self.shield_exist2.setGeometry(QtCore.QRect(590, 280, 51, 51))
        self.shield_exist2.setText("")
        self.shield_exist2.setPixmap(QtGui.QPixmap(""))
        self.shield_exist2.setScaledContents(True)
        self.shield_exist2.setObjectName("shield_exist2")

        self.information = QtWidgets.QLabel(Form)
        self.information.setGeometry(QtCore.QRect(20, 650, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.information.setFont(font)
        self.information.setObjectName("information")

        self.creator_name = QtWidgets.QLabel(Form)
        self.creator_name.setGeometry(QtCore.QRect(530, 660, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.creator_name.setFont(font)
        self.creator_name.setObjectName("creator_name")

        self.sword.clicked.connect(self.sword_button)
        self.shield.clicked.connect(self.shield_button)
        self.done.clicked.connect(self.done_button)
        self.damage = 0
        self.defense = 0
        self.is_shield1 = "No"
        self.is_shield2 = "No"
        self.player_hp_int = 500
        self.enemy_hp_int = 500
        self.player_cd = 0
        self.enemy_cd = 1
        self.enemy_move = None

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "SWORD-SHIELD"))
        self.sword.setText(_translate("Form", "SWORD"))
        self.shield.setText(_translate("Form", "SHIELD"))
        self.player_name.setText(_translate("Form", "<html><head/><body><p align=\"center\">Player 1</p></body></html>"))
        self.enemy_name.setText(_translate("Form", "<html><head/><body><p align=\"center\">Enemy</p></body></html>"))
        self.hp_text.setText(_translate("Form", "HP:"))
        self.player_hp.setText(_translate("Form", "500"))
        self.enemy_hp_text.setText(_translate("Form", "HP:"))
        self.enemy_hp.setText(_translate("Form", "500"))
        self.actions.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600; text-decoration: underline;\">Actions</span></p></body></html>"))
        self.actions_text.setText(_translate("Form", "<html><head/><body><p align=\"center\">-----<br/>---<br/>-----<br/>---<br/>-----</p></body></html>"))
        self.actions_2.setText(_translate("Form", "<html><head/><body><p align=\"center\">Choose your move</p></body></html>"))
        self.done.setText(_translate("Form", "DONE"))
        self.information.setText(_translate("Form", "<html><head/><body><p>Sword: Random damage (1-100)</p><p>Shield: Random damage absorption (1-100)</p></body></html>"))
        self.creator_name.setText(_translate("Form", 'Created By Ata DİKMEN'))

    def sword_button(self):
        _translate = QtCore.QCoreApplication.translate
        if self.player_cd == 0:
            self.shield_exist1.setPixmap(QtGui.QPixmap("sword_image.png"))
            self.shield_exist2.setPixmap(QtGui.QPixmap(""))
            self.is_shield1 = "No"
            self.enemy_cd = 0
            self.player_cd = 1
            self.damage = random.randint(1, 100)
            if self.is_shield2 == "No":
                self.enemy_hp_int -= self.damage
                if self.enemy_hp_int > 0:
                    self.actions_text.setText(_translate("Form","<html><head/><body><p align=\"center\">YOU DREW YOUR SWORD!<br/><br/>YOU HIT {} DAMAGE <br/><br/>YOUR ENEMY HAS {} HEALTH POINTS LEFT<br/>CLICK THE 'DONE' BUTTON</p></body></html>".format(str(self.damage), self.enemy_hp_int)))
                    self.enemy_hp.setText(_translate("Form", "{}".format(str(self.enemy_hp_int))))
                else:
                    self.actions_text.setText(_translate("Form","<html><head/><body><p align=\"center\">YOU DREW YOUR SWORD!<br/><br/>YOU HIT {} DAMAGE <br/><br/>YOU KILLED YOUR ENEMY. YOU WIN!</p></body></html>".format(str(self.damage))))
                    self.enemy_hp.setText(_translate("Form", "{}".format("0")))
                    self.avatar2.setPixmap(QtGui.QPixmap("avatar2_dead.jpg"))
                    self.player_cd = 1
                    self.enemy_cd = 1
                    self.sound()

            elif self.is_shield2 == "Yes":
                self.defense = random.randint(1,100)
                if self.defense > self.damage:
                    self.actions_text.setText(_translate("Form","<html><head/><body><p align=\"center\">YOU DREW YOUR SWORD!<br/><br/>THE ENEMY'S SHIELD ABSORBED ALL THE DAMAGE<br/>CLICK THE 'DONE' BUTTON</p></body></html>".format(str(self.damage), self.enemy_hp_int)))
                else:
                    self.damage -= self.defense
                    self.enemy_hp_int -= self.damage
                    if self.enemy_hp_int <= 0:
                        self.actions_text.setText(_translate("Form","<html><head/><body><p align=\"center\">YOU DREW YOUR SWORD!<br/><br/>THE ENEMY'S SHIELD REDUCED THE DAMAGE TO {}<br/><br/>YOU KILLED YOUR ENEMY. YOU WIN!</p></body></html>".format(str(self.damage))))
                        self.enemy_hp.setText(_translate("Form", "{}".format("0")))
                        self.avatar2.setPixmap(QtGui.QPixmap("avatar2_dead.jpg"))
                        self.player_cd = 1
                        self.enemy_cd = 1
                        self.sound()
                    else:
                        self.actions_text.setText(_translate("Form","<html><head/><body><p align=\"center\">YOU DREW YOUR SWORD!<br/><br/>THE ENEMY'S SHIELD REDUCED THE DAMAGE TO {}<br/><br/>YOUR ENEMY HAS {} HEALTH POINTS LEFT<br/>CLICK THE 'DONE' BUTTON</p></body></html>".format(str(self.damage), self.enemy_hp_int)))
                        self.enemy_hp.setText(_translate("Form", "{}".format(str(self.enemy_hp_int))))
        else:
            pass

    def shield_button(self):
        _translate = QtCore.QCoreApplication.translate
        if self.player_cd == 0:
            self.shield_exist1.setPixmap(QtGui.QPixmap("shield_image.png"))
            self.enemy_cd = 0
            self.player_cd = 1
            self.is_shield1 = "Yes"
            self.actions_text.setText(_translate("Form", "<html><head/><body><p align=\"center\">YOU'VE PULLED YOUR SHIELD!</p></body></html>"))
        else:
            pass

    def done_button(self):
        _translate = QtCore.QCoreApplication.translate
        if self.enemy_cd == 0:
            self.player_cd = 0
            self.enemy_cd = 1
            self.enemy_move = random.choice(["Sword","Shield","Sword"])
            if self.enemy_move == "Sword":
                self.shield_exist2.setPixmap(QtGui.QPixmap("sword_image.png"))
                self.shield_exist1.setPixmap(QtGui.QPixmap(""))
                self.is_shield2 = "No"
                self.damage = random.randint(1, 100)
                if self.is_shield1 == "No":
                    self.player_hp_int -= self.damage
                    if self.player_hp_int <= 0:
                        self.actions_text.setText(_translate("Form","<html><head/><body><p align=\"center\">THE ENEMY DREW THE SWORD!<br/><br/>YOUR ENEMY HAS HIT {} DAMAGE<br/><br/>YOUR ENEMY KILLED YOU. YOU LOST!</p></body></html>".format(str(self.damage))))
                        self.player_hp.setText(_translate("Form", "{}".format("0")))
                        self.avatar1.setPixmap(QtGui.QPixmap("avatar1_dead.jpg"))
                        self.player_cd = 1
                        self.enemy_cd = 1
                        self.sound()
                    else:
                        self.actions_text.setText(_translate("Form","<html><head/><body><p align=\"center\">THE ENEMY DREW THE SWORD!<br/><br/>YOUR ENEMY HAS HIT {} DAMAGE<br/><br/>YOU HAVE {} HEALTH POINTS LEFT</p></body></html>".format(str(self.damage), self.player_hp_int)))
                        self.player_hp.setText(_translate("Form", "{}".format(str(self.player_hp_int))))

                elif self.is_shield1 == "Yes":
                    self.defense = random.randint(1, 100)
                    if self.defense > self.damage:
                        self.actions_text.setText(_translate("Form","<html><head/><body><p align=\"center\">THE ENEMY DREW THE SWORD!<br/><br/>YOUR SHIELD HAS ABSORBED ALL THE DAMAGE</p></body></html>".format(str(self.damage), self.player_hp_int)))
                    else:
                        self.damage -= self.defense
                        self.player_hp_int -= self.damage
                        if self.player_hp_int <= 0:
                            self.actions_text.setText(_translate("Form","<html><head/><body><p align=\"center\">THE ENEMY DREW THE SWORD!<br/><br/>YOUR SHIELD REDUCED THE DAMAGE TO {}<br/><br/>YOUR ENEMY KILLED YOU. YOU LOST!</p></body></html>".format(str(self.damage))))
                            self.player_hp.setText(_translate("Form", "{}".format("0")))
                            self.avatar1.setPixmap(QtGui.QPixmap("avatar1_dead.jpg"))
                            self.player_cd = 1
                            self.enemy_cd = 1
                            self.sound()
                        else:
                            self.actions_text.setText(_translate("Form","<html><head/><body><p align=\"center\">THE ENEMY DREW THE SWORD!<br/><br/>YOUR SHIELD REDUCED THE DAMAGE TO {}<br/><br/>YOU HAVE {} HEALTH POINTS LEFT</p></body></html>".format(str(self.damage), self.enemy_hp_int)))
                            self.player_hp.setText(_translate("Form", "{}".format(str(self.player_hp_int))))
            elif self.enemy_move == "Shield":
                self.shield_exist2.setPixmap(QtGui.QPixmap("shield_image.png"))
                self.is_shield2 = "Yes"
                self.actions_text.setText(_translate("Form","<html><head/><body><p align=\"center\">THE ENEMY HAS PULLED HIS SHIELD!</p></body></html>"))
        else:
            pass

    def sound(self):
        winsound.PlaySound("Mario_Sound", winsound.SND_FILENAME)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
