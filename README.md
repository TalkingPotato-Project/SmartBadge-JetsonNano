# 어린이 스마트 배지 <br> 
**영상 및 위치정보에 기반한 어린이 사고 예방 시스템**

> 🏆 제 9회 대한전기학회 산업전기위원회 대학생 작품경진대회 **대상** 수상 🏆


<br> 

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

### 4. 결론
- [ 결론 ](https://github.com/)


<br>

## 1. 소개 - [YouTube 소개 영상](https://www.youtube.com/watch?v=Ps39QcEkKhw)

Jetson Nano에 기반하여 어린이 안전을 위한 스마트 배지를 구현한다. 

꾸준히 발생하고 있는 실종 아동 문제와 어린이 교통사고 문제는 어린이들의 안전을 위협하고 있으며, 아이가 있는 보호자들의 불안감을 야기한다. 

이러한 문제를 해결하기 위해 제안된 어린이 스마트 배지의 시스템은 세 가지로 구성되어 있다.

- 어린이용 배지
- Server
- 보호자용 App

<h4>주요 기술 및 기능</h4>


- Semantic Segmentation 기술을 사용한 상황별 알림 기능을 통해 어린이들의 교통안전 의식을 향상시키고 무단횡단을 예방한다. 
  - 아이가 길에서 어느 방향을 바라보고 있는지 판단하여 상황에 따라 다르게 저장되어 있는 보호자 음성을 어린이들에게 직접적으로 알림을 줌
  - 직접 보호자가 녹음한 음성 알림으로 어린이들은 알림에 더욱 집중할 수 있다.
- GPS를 이용하여 보호자 App에서 안전 구역 설정 및 아이의 실시간 위치를 파악하고 안전 구역 이탈 시 알림을 받을 수 있어 범죄를 예방하거나 문제 발생 시 빠른 대처가 가능하다.
<br>

<p align="center"><img src="https://user-images.githubusercontent.com/50138845/131224422-3c02967e-114d-4ed5-b622-8628487b54a6.gif"></p>

<br>

<h4>하드웨어 구성</h4>

![hardware](https://user-images.githubusercontent.com/46085058/131228189-b2cbab14-fbdb-4776-8cb0-7cae427686e3.png)

<br>
<h4>예시</h4>

![image](https://user-images.githubusercontent.com/46085058/131228361-7a1b7f6a-668e-44c4-8859-dfd7f92bed66.png)

<br>

## 2. 개발 환경

**시스템 구성도**

<p align="center"><img src="https://user-images.githubusercontent.com/46085058/131226185-d0ff5001-6574-49ce-b798-756dc0982f58.png"></p>


<br>


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

![image](https://user-images.githubusercontent.com/50138845/139537458-52f63993-b52c-4d77-a196-f248c197574a.png)

학습 데이터로 사용할 이미지를 Labelme에서 Class마다 영역을 나누어 Label을 지정해준다. Class는 Background, Roadway, Sidewalk, Crosswalk로 총 4개로 구성된다.

<br><br><br>

### 도로 구분 - Semantic Segmentation

어린이의 교통안전의식 향상과 무단횡단을 방지 기능을 구현하기 위해 Semantic Segmentation 기술을 사용하였으며 FCN(Fully Convolutional Networks) 모델을 사용하였다.
    
<p align="center"><img src="https://user-images.githubusercontent.com/50138845/131224452-bf08d2f9-c3f1-420e-8bad-b29fb6d8fd95.png"></p>

카메라 모듈로 정면을 촬영하여 들어오는 Input data로 Semantic Segmentation 기술을 통하여 각 픽셀의 Class들을 알 수 있고, 판단 영역을 잡아 해당 영역에 가장 많이 있는 Class가 무엇인지 계산하여 해당 Class로 어린이가 바라보고 있는 도로의 유형을 판단한다.

<p align="center"><img src="https://user-images.githubusercontent.com/50138845/131224473-da4daf74-8bcd-4b8b-8a46-714eddaa6f6b.png"></p>

어린이가 바라보고 있는 도로의 유형을 판단하기 위한 영역은 위 그림과 같이 Input data의 가로와 높이를 크게 5x5로 나누어 (5, 3) 위치를 판단 영역으로 설정하였다. 
Semantic Segmentation을 통하여 알 수 있는 픽셀 당 Class는 행렬로 저장이 되고, (5, 3) 구역 안에 행렬로 저장되어 있는 Class 값들 중 가장 많이 차지하고 있는 Class로 어린이가 바라보고 있는 곳의 도로 유형을 판단한다.
<br><br><br>
#### 도로의 유형에 따른 알림

| <center>도로 유형</center>  | <center>사진</center>  | <center>설명</center>  |
| ------------ | ------------ |------------ |
| 인도  | ![image](https://user-images.githubusercontent.com/50138845/131224566-29cf4122-abce-4271-84b7-d03860424485.png)  | 판단 영역이 인도로 판단될 경우 어린이가 인도 위에서 안전하게 보행하고 있다고 판단하며 별도의 알림이 울리지 않는다.  |
| 횡단보도  | ![image](https://user-images.githubusercontent.com/50138845/131224619-3b1dfb01-04a9-4a6c-a022-f6c228a01a1d.png)  | 판단 영역이 횡단보도로 판단될 경우 어린이가 횡단보도 앞에 있다고 판단하며 보호자의 음성 알림( 예시: “00아 초록불 일 땐 양옆을 살피고 빨간불에는 멈춰!” )이 울린다.  |
| 도로  | ![image](https://user-images.githubusercontent.com/50138845/131224649-bd309439-b6bf-402c-8710-baf924f22166.png)|  판단 영역이 차도로 판단될 경우 어린이가 차도를 향해서 보행하고 있어 위험하다고 판단하며 보호자의 음성 알림(예시: “00아 도로에서 뛰면 위험해 횡단보도로 건너”)이 울린다. |
|   | <center>무단횡단의 경우</center>|  판단 영역이 차도로 판단된 후 가속도 센서의 변화가 일정량 감지되면 어린이가 차도 방향으로 무단횡단을 시도하는 것으로 판단되어 보호자의 음성 알림(예시: “00아 무단횡단은 안돼! 횡단보도로 건너”)이 울린다. |

<br><br><br>



<br>


### Application & Server

[Application Repository](https://github.com/TalkingPotato-Project/SmartBadge-App) <br>
[Server Repository](https://github.com/TalkingPotato-Project/SmartBadge-Server)

### Application

####  보호자용 App 메인화면과 안심 구역 관리
<p align="center"><img src="https://user-images.githubusercontent.com/46085058/131225741-fecc12e2-7cff-46a6-9718-7012015e5c7c.png"></p>

보호자용 App의 메인화면(좌)과 아이가 이동한 영역에 대해 안심 구역을 설정한 화면(우)이다. 메인화면의 가장 왼쪽에 있는 안심 구역 관리 버튼을 클릭하면 아이의 안심 구역을 추가, 삭제가 가능하고, 아이의 무단횡단 기록을 열람할 수 있다.
<br><br><br>

#### 안심 구역 이탈 및 추가
<p align="center"><img src="https://user-images.githubusercontent.com/46085058/131225770-df8e1c97-4ad3-4098-860c-cbc2b68c7179.png"></p>
<p align="center"><img src="https://user-images.githubusercontent.com/46085058/131226023-ad2896a7-e5d1-4256-b6e6-6508357f65d1.png"></p>

아이가 안심 구역을 이탈했을 경우 안심 구역을 추가, 삭제할 수 있는 화면이다. 아이가 안심 구역을 이탈하면 보호자용 App을 통하여 보호자에게 알림이 가고, 이탈한 경로가 빨간색 선으로 표시가 된다. 이 경로를 안심 구역으로 추가를 하거나 삭제할 수 있다.
<br><br><br>

#### 무단횡단 기록 열람 & 상황별 보호자 음성 알림 녹음
<p align="center"><img src="https://user-images.githubusercontent.com/46085058/131225885-7660cf8f-354d-4f4a-a4d0-f2faf28f41da.png">
    <img src="https://user-images.githubusercontent.com/46085058/131225876-b817298a-d067-49bf-9a2b-0e4d37932860.png"></p>

아이의 무단횡단 기록을 열람할 수 있는 화면이다. 아이가 무단횡단을 할 시, 그 위치 정보가 서버에 저장되고 보호자용 App에서 보호자가 무단횡단 위치와 당시 시간대를 알 수 있다.
<br>
어린이 스마트 배지에서 울리게 될 알림을 녹음하는 화면이다. 차도일 때, 횡단보도일 때, 무단횡단할 때로 세 가지의 경우로 나누어져 있다. 보호자용 App에서 알림을 녹음하면 서버에 녹음 파일이 저장되고 어린이 스마트 배지에서 보호자 음성 알림을 재생할 수 있다.
<br><br><br>

<br>

### Server

#### WAS 서버 구조

<p align="center"><img src="https://user-images.githubusercontent.com/46085058/131227251-0de08596-429b-4f85-a102-29ce8e630cea.png"></p>

어린이 스마트 배지로 HTTP 통신을 수행하기 위해 웹 서버는 Nginx를 사용하였고, 어린이 스마트 배지에서 실시간 위치 정보를 서버로 전송하기 때문에 REST 방식의 서버를 설계할 수 있도록 애플리케이션 프레임워크로 Django restframework를 사용하였다. 미들웨어로는 Nginx와 Django의 호환성이 높은 Gunicorn WSGI를 사용하였다. Gunicorn은 Nginx와 함께 역방향 프록시 구성으로 배포되며 Nginx와 Django framework의 사이에서 요청과 응답을 전달한다.
<br><br><br>

#### Server DB Table

<p align="center"><img src="https://user-images.githubusercontent.com/46085058/131227274-7a273252-7f5a-44dd-bef5-66b8e2a9fd57.png"></p>

서버의 DB(Data Base)는 MySQL DB를 사용하였다. 서버의 DB Table은 위 <그림 10>과 같다. DB에는 어린이 스마트 배지 구동을 위해 사용자 정보를 저장하는 users table에 어린이 스마트 배지의 일련번호, 사용자 고유 ID 값을 저장한다. 저장된 사용자 정보는 Application에서 데이터를 요청할 때 인증 절차에 사용된다. voicefile table은 보호자가 Application에서 상황별 알림을 녹음한 파일이 저장된다. gpsroute, jaywalking, newroute table의 경우 어린이 보행 안전 확보와 실종 사고를 예방하기 위해서 GPS 정보 저장의 목적으로 활용된다.
<br><br><br>


#### GPS정보 분석 및 안심 구역 이탈 감지

안심구역 PolyLine 생성

<br>

<p align="center"><img src="https://user-images.githubusercontent.com/46085058/131227287-35c5d20e-1df3-4597-850a-845ad70a5646.png"></p>

어린이 스마트 배지는 실시간으로 GPS 정보를 서버로 전송한다. 서버로 전송된 GPS 정보는 안심 구역이 생성되어 있지 않았을 경우 초기 안심 구역 설정에 필요함으로 해당 GPS 정보를 별도의 DB에 저장한다. 
<br>

안심 구역은 생성 시에 별도로 저장된 GPS 정보를 기반으로 중복되는 불필요한 정보를 그림과 같이 제거한 후에 PolyLine 객체로 저장한다. PolyLine으로 저장된 안심 구역은 보호자용 Application에서 시각화하여 보여줄 수 있도록 하였다.
<br><br><br>


Ray Casting 알고리즘

<br>

<p align="center"><img src="https://user-images.githubusercontent.com/46085058/131227347-c85f7380-508a-4616-8449-9c09ee5b71d2.png"></p>

안심 구역 이탈 감지의 경우 저장된 안심 구역 PolyLine객체를 일정 범위를 가지고 있는 Polygon객체로 변환하는 과정을 우선 수행한다. 이후 어린이 스마트 배지의 실시간 GPS 정보가 서버로 들어오면 Ray Casting 알고리즘을 수행하여 그림과 같이 교차점의 수가 홀수 개일 때 해당 GPS 정보가 안심 구역 내부에 있다고 판단하여 Safe State를 True로, 교차점의 수가 0 또는 짝수 개일 때 외부에 있다고 판단하여 False를 반환하여 안심 구역 이탈을 감지한다.
안심 구역을 이탈하였을 경우 이탈하는 지점부터  GPS 정보를 DB에 저장한다. 이후 이탈한 GPS 정보에 대해서 기존 안심 구역에 추가 또는 삭제를 할 수 있으며, 추가의 경우 기존 안심 구역의 PolyLine객체에 가장 근접한 지점을 찾은 후 안심 구역 생성과 동일한 알고리즘을 수행하여 안심 구역을 갱신한다.
<br><br><br>


### Sensors

[Accelerometer_ADXL345](https://github.com/TalkingPotato-Project/SmartBadge-JetsonNano/tree/main/Sensors/Accelerometer_ADXL345 "Accelerometer_ADXL345") <br>
[GPS_NEO-7m](https://github.com/TalkingPotato-Project/SmartBadge-JetsonNano/tree/main/Sensors/GPS_NEO-7m "GPS_NEO-7m")


<br> 

## 4. 결론


어린이 스마트 배지는 Jetson nano에 카메라와 GPS 모듈을 사용하여 어린이의 시야에서 도로 유형 판별에 따른 알림 및 안심 구역 생성과 이탈을 감지하기 위한 기능을 구현하였다. 

Semantic Segmentation을 통해 도로의 유형을 구분하고 어린이에게 도로의 위험성을 사전에 인지할 수 있도록 하였으며, 어린이의 이동 경로를 기반으로 하는 GPS 정보를 분석하여 안심 구역을 스스로 생성하고 이탈을 감지하도록 하였다. 보호자용 App과 서버를 통해 어린이 스마트 배지와 통신하며 각종 알림에 대한 보호자의 목소리 녹음과 이탈 시 알림을 받을 수 있도록 하였다.

실험을 통해 제안 시스템의 안정성과 정확성을 확인하였고 어린이 보행 안전 및 안심 구역 이탈 감지를 실시간으로 할 수 있음을 보였다. 이를 통해 어린이 사고 예방을 위한 시스템으로 활용 가능할 것이다.

더 많은 영상 데이터 셋을 구축하여 Semantic Segmentation 정확도를 향상시키고, 직접적으로 무단횡단을 방지할 수 있는 방법과 어린이의 이동 경로를 실시간으로 추정하여 이상 경로에 대한 위험성을 사전에 분석하는 방법 연구를 지속적으로 수행할 예정이다.


<p align="center"><img src="https://user-images.githubusercontent.com/50138845/131226399-d204a2b7-89fe-48af-8231-feb58aafabe1.png" width = 300px></p>
