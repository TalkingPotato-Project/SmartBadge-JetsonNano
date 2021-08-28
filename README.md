## SmartBadge <br> 영상 및 위치정보에 기반한 어린이 사고 예방 시스템 
### 요구사항
* [NVIDIA Jetson Nano Development Kit-B01](https://developer.nvidia.com/embedded/jetson-nano-developer-kit)

    ![jetsnoback](https://user-images.githubusercontent.com/46085058/131222247-93795620-346a-4c82-a206-72a8e600f5a6.png)

## 목차
### 1. 소개
- [ 프로젝트 내용 소개 ](https://github.com/)


### 2. 개발 환경
- [ 사전 설정 및 환경 구축 ](https://github.com/)

### 3. 기능
- [ 데이터셋 구축 - Lableme ](https://github.com/)
- [ 도로 구분 - Semantic Segmentation ](https://github.com/)
- [ Sensors ](https://github.com/)
- [ App & Server ](https://github.com/)

<br>

## 1. 소개
(프로젝트 내용 소개)<br>
Jetson Nano에 기반하여 어린이 안전을 위한 스마트 배지를 구현한다. 꾸준히 발생하고 있는 실종 아동 문제와 어린이 교통사고 문제는 어린이들의 안전을 위협하고 있으며, 아이가 있는 보호자들의 불안감을 야기한다. 이러한 문제를 해결하기 위해 제안된 어린이 스마트 배지의 시스템은 어린이용 배지, 서버, 보호자용 App으로 구성되어 있으며 두 가지 주요 기술을 사용한다. Semantic Segmentation 기술을 사용한 상황별 알림 기능을 통해 어린이들의 교통안전 의식을 향상시키고 무단횡단을 예방한다. 또한, GPS를 이용하여 보호자 App에서 안전 구역 설정 및 아이의 실시간 위치를 파악하고 안전 구역 이탈 시 알림을 받을 수 있어 범죄를 예방하거나 문제 발생 시 빠른 대처가 가능하다.
<br>

<p align="center"><img src="https://user-images.githubusercontent.com/50138845/131224422-3c02967e-114d-4ed5-b622-8628487b54a6.gif"></p>


## 2. 개발 환경

![image](https://user-images.githubusercontent.com/46085058/131224518-ddb7671a-731f-4965-9f5d-7ece7107c7bb.png)

| **Category**  | <center>**Tools**</center>  | **Version**  |
| :------------: | ------------| :------------: |
| **Jetson-nano** | Image  |  jetson-nano-jp451  |
|   | python  | 3.6.9  |
| **Application** | AndroidStudio  |  4.1.0 |
|   | compileSdkVersion  | 30  |
|   | buildToolsVersion  | 30.0.2  |
| **Server**  | OS  | CentOS 7.9 2009  |
|   | Django | 3.2.2  |
|   | DjangoRestframework  |  3.12.4 |
|   | Gunicorm  | 20.1.0  |
|   | MySql-Client  |  2.0.3 |
| **DataBase**  | MySql  | 8.0.25  |

<br>


## 3. 기능

### 데이터셋 구축 - Lableme

![image](https://user-images.githubusercontent.com/46085058/131225972-01ad42b1-3b99-48ff-8c92-be0b2f9d6917.png)
![image](https://user-images.githubusercontent.com/46085058/131225993-f332b9b3-caaa-41f8-96ee-80cb4d5ff06e.png)

<br>

### 도로 구분 - Semantic Segmentation

어린이의 교통안전의식 향상과 무단횡단을 방지 기능을 구현하기 위해 Semantic Segmentation 기술을 사용하였으며 FCN(Fully Convolutional Networks) 모델을 사용하였다.
    
<p align="center"><img src="https://user-images.githubusercontent.com/50138845/131224452-bf08d2f9-c3f1-420e-8bad-b29fb6d8fd95.png"></p>

카메라 모듈로 정면을 촬영하여 들어오는 Input data로 Semantic Segmentation 기술을 통하여 각 픽셀의 Class들을 알 수 있고, 판단 영역을 잡아 해당 영역에 가장 많이 있는 Class가 무엇인지 계산하여 해당 Class로 어린이가 바라보고 있는 도로의 유형을 판단한다.

<p align="center"><img src="https://user-images.githubusercontent.com/50138845/131224473-da4daf74-8bcd-4b8b-8a46-714eddaa6f6b.png"></p>

어린이가 바라보고 있는 도로의 유형을 판단하기 위한 영역은 위 그림과 같이 Input data의 가로와 높이를 크게 5x5로 나누어 (5, 3) 위치를 판단 영역으로 설정하였다. 
Semantic Segmentation을 통하여 알 수 있는 픽셀 당 Class는 행렬로 저장이 되고, (5, 3) 구역 안에 행렬로 저장되어 있는 Class 값들 중 가장 많이 차지하고 있는 Class로 어린이가 바라보고 있는 곳의 도로 유형을 판단한다.
<br>
##### 도로의 유형에 따른 알림

| <center>도로 유형</center>  | <center>사진</center>  | <center>설명</center>  |
| ------------ | ------------ |------------ |
| 인도  | ![image](https://user-images.githubusercontent.com/50138845/131224566-29cf4122-abce-4271-84b7-d03860424485.png)  | 판단 영역이 인도로 판단될 경우 어린이가 인도 위에서 안전하게 보행하고 있다고 판단하며 별도의 알림이 울리지 않는다.  |
| 횡단보도  | ![image](https://user-images.githubusercontent.com/50138845/131224619-3b1dfb01-04a9-4a6c-a022-f6c228a01a1d.png)  | 판단 영역이 횡단보도로 판단될 경우 어린이가 횡단보도 앞에 있다고 판단하며 보호자의 음성 알림( 예시: “00아 초록불 일 땐 양옆을 살피고 빨간불에는 멈춰!” )이 울린다.  |
| 도로  | ![image](https://user-images.githubusercontent.com/50138845/131224649-bd309439-b6bf-402c-8710-baf924f22166.png)|  판단 영역이 차도로 판단될 경우 어린이가 차도를 향해서 보행하고 있어 위험하다고 판단하며 보호자의 음성 알림(예시: “00아 도로에서 뛰면 위험해 횡단보도로 건너”)이 울린다. |
|   | <center>무단횡단의 경우</center>|  판단 영역이 차도로 판단된 후 가속도 센서의 변화가 일정량 감지되면 어린이가 차도 방향으로 무단횡단을 시도하는 것으로 판단되어 보호자의 음성 알림(예시: “00아 무단횡단은 안돼! 횡단보도로 건너”)이 울린다. |
<br>

### Sensors

[Accelerometer_ADXL345](https://github.com/TalkingPotato-Project/SmartBadge-JetsonNano/tree/main/Sensors/Accelerometer_ADXL345 "Accelerometer_ADXL345") <br>
[GPS_NEO-7m](https://github.com/TalkingPotato-Project/SmartBadge-JetsonNano/tree/main/Sensors/GPS_NEO-7m "GPS_NEO-7m")
<br>
### App & Server

#### 사용자 인터페이스(User Interface)

##### 보호자용 App 메인화면과 안심 구역 관리
![image](https://user-images.githubusercontent.com/46085058/131225741-fecc12e2-7cff-46a6-9718-7012015e5c7c.png)

보호자용 App의 메인화면(좌)과 아이가 이동한 영역에 대해 안심 구역을 설정한 화면(우)이다. 메인화면의 가장 왼쪽에 있는 안심 구역 관리 버튼을 클릭하면 아이의 안심 구역을 추가, 삭제가 가능하고, 아이의 무단횡단 기록을 열람할 수 있다.


##### 안심 구역 이탈 및 추가
![image](https://user-images.githubusercontent.com/46085058/131225770-df8e1c97-4ad3-4098-860c-cbc2b68c7179.png)
![image](https://user-images.githubusercontent.com/46085058/131226023-ad2896a7-e5d1-4256-b6e6-6508357f65d1.png)

아이가 안심 구역을 이탈했을 경우 안심 구역을 추가, 삭제할 수 있는 화면이다. 아이가 안심 구역을 이탈하면 보호자용 App을 통하여 보호자에게 알림이 가고, 이탈한 경로가 빨간색 선으로 표시가 된다. 이 경로를 안심 구역으로 추가를 하거나 삭제할 수 있다.

##### 무단횡단 기록 열람 & 상황별 보호자 음성 알림 녹음
![image](https://user-images.githubusercontent.com/46085058/131225885-7660cf8f-354d-4f4a-a4d0-f2faf28f41da.png)
![image](https://user-images.githubusercontent.com/46085058/131225876-b817298a-d067-49bf-9a2b-0e4d37932860.png)

아이의 무단횡단 기록을 열람할 수 있는 화면이다. 아이가 무단횡단을 할 시, 그 위치 정보가 서버에 저장되고 보호자용 App에서 보호자가 무단횡단 위치와 당시 시간대를 알 수 있다.

어린이 스마트 배지에서 울리게 될 알림을 녹음하는 화면이다. 차도일 때, 횡단보도일 때, 무단횡단할 때로 세 가지의 경우로 나누어져 있다. 보호자용 App에서 알림을 녹음하면 서버에 녹음 파일이 저장되고 어린이 스마트 배지에서 보호자 음성 알림을 재생할 수 있다.




