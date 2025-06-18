## Intro

This is the official Github repository for The Adakademy Team, before known as Adagroup, conformed by Jesser Palma, Jesús Alcalá and Hector Cartagena. This repository contains all the code, documentation, and resources for our project, HALBI. This is our third year participating in WRO

---
# Team Members

* Jesús Alcalá, 20 years old, jdam5000@gmail.com
* Héctor Cartagena, 18 years old, cartagenahector0608@gmail.com
* Jesser Palma, 20 years old, jssrpalma3@gmail.com
---
# 📖 Content of README 📖
* **[Hardware](#hardware)**
  * [Components](#components)
  * [Components description](#components-description)
  * [Wiring Diagram](#wiring-diagram)
  * [Mobility Management](#-mobility-management-)
    * [Chassis](#chassis)
    * [Design](#design)
    * [Motors](#motors)
  * [Power and Sense Management](#-power-and-sense-management-)
    * [Power and Wiring](#power-and-wiring)
    * [Sensors](#sensors)
    * [Schematic](#schematic)
* **[Software](#-software-)**
  * [Initialization and Connection Process](#-initialization-and-connection-process-)
  * [Object Management](#object-management)
    *  [Object Detection](#object-detection--open-challenge--obstacle-challenge-)
    *  [Wall Detection/Management](#wall-detectionmanagement--open-challenge--obstacle-challenge-)
    *  [Signal Pillar Detection/Management](#signal-pillar-detectionmanagement--obstacle-challenge-)
    *  [Turning (Open Challenge)](#turning--open-challenge-)
    *  [Turning (Obstacle Challenge)](#turning--obstacle-challenge-)
    *  [Parking Lot Detection/Management](#parking-lot-detectionmanagement--obstacle-challenge-)
    *  [Three-Point Turn](#three-point-turn--obstacle-challenge-)
    *  [Backing Up](#backing-up--obstacle-challenge-)
    *  [Potential Improvement: Stuck Detection](#potential-improvement-stuck-detection--open-challenge--obstacle-challenge-)
* **[Assembly Instructions](#-complete-assembly-instructions-)**
---
# Hardware
---
## Components
| Cantidad | Producto               | Precio Unitario | Total |
|----------|------------------------|----------------|-------|
| 1        | [Raspberry Pi 4 B](https://www.amazon.com/Raspberry-aleaci%C3%B3n-resistente-refrigerada-ventilador/dp/B07XTRK8D4/ref=sxin_16_pa_sp_search_thematic_sspa?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&content-id=amzn1.sym.2da95b6c-f59a-4699-bc43-d0ff036c6388%3Aamzn1.sym.2da95b6c-f59a-4699-bc43-d0ff036c6388&crid=1MNN6HXZPRQX8&cv_ct_cx=raspberry%2Bpi%2B4&keywords=raspberry%2Bpi%2B4&pd_rd_i=B07XTRK8D4&pd_rd_r=8fd6db19-a9bf-49f2-bed5-d85f62162bf9&pd_rd_w=PCH4o&pd_rd_wg=RHQgL&pf_rd_p=2da95b6c-f59a-4699-bc43-d0ff036c6388&pf_rd_r=PBJ9HR8999TXWA966P2T&qid=1749992437&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sprefix=raspberry%2Caps%2C240&sr=1-1-6024b2a3-78e4-4fed-8fed-e1613be3bcce-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9zZWFyY2hfdGhlbWF0aWM&th=1)       | $110.00        | $110.00 |
| 1        | [Car chassis with motor and servo](https://www.amazon.com/-/es/fischertechnik-Maker-Kit-Car-571900/dp/B0CY31DGT1/ref=sr_1_1?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1U5LDJG1N012B&dib=eyJ2IjoiMSJ9.A4y-GcKAwAbaTNsidmYvDQ.2Dl1_C7M_3siNlFrrKAdwcWGiPjo24JfKghV4CarK_E&dib_tag=se&keywords=maker%2Bkit%2Bcat%2Bfischertechnik&qid=1749992612&sprefix=maker%2Bkit%2Bcat%2Bfishertecnk%2Caps%2C160&sr=8-1&th=1)            | $152.00        | $152.00 |
| 4        | [18650 Batteries x 2](https://articulo.mercadolibre.com.ve/MLV-822728792-bateria-de-litio-recargable-18650-37v-7800mah-_JM?searchVariation=187506651449#polycard_client=search-nordic&searchVariation=187506651449&position=19&search_layout=grid&type=item&tracking_id=f46731bc-e110-4c1c-9e3a-39f03dcf9778)        | $10.00         | $20.00 |
| 1        | [Webcam logitech](https://www.amazon.com/Logitech-correcci%C3%B3n-funciona-Facetime-port%C3%A1til/dp/B085TFF7M1/ref=sr_1_2_sspa?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3TDC9UPMF20PS&dib=eyJ2IjoiMSJ9.xVtRFzFOfA678C9UfJ2P5Dh7j6AKD4iv-V9zhwnZJXYCh_6zM88bwBS9VWgL2w_3mGaa2uxe9o4cdBsL_BgvjWHHZFlQwZxXSu3xHKbtXKtLgqanXwZcBUa0IPpJwXPXFle4j_EGkZhlpLKyFrCyaBbO1DKFYX44vGxHypHBBBW-Tg9L1-hBbx0JGQr6ErvXTTHn_He7u6W-2lBIAIKn1cV0Sgqn6bM11UwhxpLHdY8.GIJKphlEnDWzfzEERyJukzgF15AKXsN6z6yUqVvDWP0&dib_tag=se&keywords=webcam%2Blogitech&qid=1750028423&sprefix=webcam%2Blogitech%2Caps%2C324&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1)        | $70.00         | $70.00 |
| 1        | [MT6068](https://www.amazon.com/-/es/Buying-M%C3%B3dulo-impulso-ajustable-MT3608/dp/B0CWKWX7QC/ref=sr_1_1?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3AMK4Y558HYRY&dib=eyJ2IjoiMSJ9.TLalRqJgBH_tYg3eQzefQNBWcCAoerGOdsZZi5tRkJtDW1CjUQosN4toICQahARr.I6Dv41TBneu-vEf_xEvgYoSrcdCVc65wJ83TyWypJHQ&dib_tag=se&keywords=mt3068&qid=1749993307&sprefix=mt3068%2Caps%2C191&sr=8-1)                 | $3.00          | $3.00  |
| 1        | [L298N](https://www.amazon.com/-/es/WWZMDiB-L298N-controlador-Arduino-Raspberry/dp/B0CR6BX5QL/ref=sr_1_4?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3O8OXGKCCVRG0&dib=eyJ2IjoiMSJ9.hK2FjV8Ukp8CCyVTI1seMk4n3aguoO_lNXX3xoiH-O0C4rrvapYby0KxsXYQdeAe863BgigxTsz1ePawqec8Hh-ZvnLMo-m-4Dm_xbIy8313Qvap61RJcd5w5fRsxA1Mfu7r-1bPw7I6tgDfFY8-XvbRp4S63ohCGnn4r_olt3NPelIGMHtKNp3R0LG1qMBP1e27x9q6fx21i5dQHcNxvQLKsGfCJHzstSjLouT-lF4.GfRYImaJhtuQGrdEbIedHfK0ZnReNVJ_VW1xuDtjz-4&dib_tag=se&keywords=l298n&qid=1749993492&sprefix=l298n%2Caps%2C179&sr=8-4)                  | $5.00          | $5.00  |
| 1        | [Arduino nano](https://www.amazon.com/-/es/Nano-conexi%C3%B3n-compatible-Arduino-V3-0/dp/B0B42GRG15/ref=sr_1_2?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=XW2BW8O1LXM1&dib=eyJ2IjoiMSJ9.qqetOTfNU56DCiKxDKpSY1mJEp8ImS6fK8GCDePazTZaNWy--wqAeFwbylHjbgMSjt8DkzFqzdbxxYSuczs_68pbBBsiqJ6JERyDANoDy1gFkr6ldjTNF-jhcupMFGeJYIE2pryL8jTW0DCCXmgjpUt_ZpGP6j7KaDwpF--Tap-TNBCnpWQudo4_N5-gKTl1qrjA9gm8z87yWbz5P9jGuOvQq81twJbp41PbsbeNKyM.VhK3Ex_WQ2P9kw3wiIa67gyryce4fQk7YtvEOlWEpdY&dib_tag=se&keywords=arduino+nano+usb+c&qid=1749993530&sprefix=arduino+nano+usb+c%2Caps%2C198&sr=8-2)           | $10.00         | $10.00 |
| 2        | [LX-2BUPS 5v](https://www.amazon.com/-/es/Bater%C3%ADa-M%C3%B3dulo-Cargador-Tablero-Indicador/dp/B0CGZS38QR/ref=sr_1_1?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=136Q8NU91WK25&dib=eyJ2IjoiMSJ9.OUZ7CB2S6RhhunyygWStlhYXdkOxEQWEOd7igJQg-ILCCJFEW-Is87jcLbWIrBYqBUWPaTZceymcS13W2cNtIA.zeXlgUhXAuX3iUN4TpHTLoBrpBR5GAd59arz0m_-F44&dib_tag=se&keywords=lx-2bups&qid=1749991945&sprefix=lx-2bups%2Caps%2C289&sr=8-1&th=1)               | $5.24          | $10.48 |
| 2        | [USB cable type C](https://www.amazon.com/paquete-cables-trenzados-iPhone-Samsung/dp/B0DPMQ7291/ref=sr_1_2_sspa?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=19WFOH9SGQR6X&dib=eyJ2IjoiMSJ9.TwlOm7HeKVsOKER2sTeYNLD5mWAyTg5X856GRR8FkQvdG6_mf3AkJUFATBnv2BeM8xp9pvV-C07pI8XJwoQ_eKhFW_LFDsdW4gMXxY4SR16LNgk9hBwUKvpjZFP6bFsEPKocQuodZaAIRYU69ZSXUM4tDsU4ICjfgal6OKZ0AduJXFmkanzaBUevDxYOerGFGKB3YJBU--yu-UaFZyqTN1Tva5bVN1G6vEmKS4970rU.FvhJ8ACjur6SL9B8e6yG-afZRtFQW6M1iDPJC9vrJN0&dib_tag=se&keywords=usb%2Bcable%2BC&qid=1749992275&sprefix=usb%2Bcable%2Bc%2Caps%2C204&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1)       | $6.00          | $12.00 |
| 2        | ON OFF Switch     | $2.5          | $5.00 |
| **Total** |                        |                | **$397.48** |

---
## Components description

### Raspberry PI 4 B 🚀 

The Raspberry Pi 4 Model B  is a powerful, credit-card-sized single-board computer (SBC)  developed by the Raspberry Pi Foundation. It is widely used in robotics, IoT projects, and embedded systems due to its versatility, performance, and affordability. 

![Raspberry](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR97vGNS_Bob3FpycF1ZooG3lmox1eXxC0DyA&s)

Our strategy is centered on computer vision algorithms developed by us using **[Opencv](https://opencv.org/)** with python, for that reason we have choose this computer given that have a low electrcity consumption (5v 3A) contrary to the pi 5 (5V 5A 😬 To high!) besides is better option that the pi 3 B that we used the last time

---
### Fischertechnik kit 🏎️
The Fischertechnik Maker Kit Car is a pre-assembled chassis that provides a solid foundation for creating functional models or prototypes of vehicles. It includes essential components such as wheels, motors, axles, and structural elements that allow users to build a stable base for their projects. The kit is compatible with various motors, sensors, and other electronic components, making it ideal for integrating advanced functionalities like autonomous driving, obstacle avoidance, or remote control. The design is modular, enabling easy modifications and upgrades as needed. This flexibility allows users to experiment with different configurations and mechanical setups without needing to start from scratch.

Kits like this are ideal for teams new to robotics because they eliminate the need for extensive mechanical assembly or 3D modeling skills. By using a pre-assembled kit, you can focus on higher-level tasks such as programming, sensor integration, and algorithm development without worrying about building the physical structure from scratch. This approach is particularly beneficial for educational purposes, as it allows students to quickly prototype ideas and test concepts without getting bogged down by mechanical complexities. Additionally, many international teams use similar kits, making it a widely accepted and practical choice for competitions like the World Robot Olympiad (WRO).

![halbi](https://media.fischer.group/v7/_pim-media-prod_/Product%20Pictures/Product%20Pictures%20fischertechnik/W1_P_P_571900_CAR.jpg?trim=5&func=fit&bg_colour=fff&org_if_sml=0&w=638&h=448.875)

While pre-assembled kits offer convenience, designing and 3D-printing your own chassis provides several advantages. First, custom chassis designs allow for greater flexibility and optimization, enabling you to tailor the vehicle to specific requirements such as weight distribution, component placement, and cost-efficiency. A well-designed custom chassis can also be more durable and reliable than off-the-shelf kits, which may have fragile parts that are not easily replaceable. Furthermore, creating your own chassis fosters deeper learning in mechanical engineering, CAD modeling, and prototyping—skills that are highly valued in robotics and engineering competitions. While it requires more time and technical expertise upfront, the ability to iterate and refine your design based on testing results leads to a more robust and competitive robot. Ultimately, while pre-assembled kits are great for getting started, building your own chassis offers superior customization, cost savings, and educational value, making it the preferred choice for advanced teams aiming to push the boundaries of innovation in the WRO FE category.

---
### Li-on 18650 Batteries, LX-2BUPS MT3068 🔋

The robot uses two 18650 Li-ion batteries  combined with an LX-2BUPS MT3068 power management module , which allows the system to function without complex circuitry or custom-built charging solutions. This setup provides a stable power source for both the Raspberry Pi and motor driver, making it suitable for teams without advanced electronics experience. The LX-2BUPS module acts as a UPS (uninterruptible power supply), ensuring smooth transitions between charging and discharging states. However, this configuration has some limitations: the 18650 batteries are relatively large, making space management within the chassis challenging. Additionally, these batteries have limited runtime when powering high-consumption components like the Raspberry Pi, especially during intensive tasks such as image processing. 

To address voltage requirements for the motors, we included a step-up module to boost the output to 11.24V , allowing the motors to operate at optimal speed. While this setup works well for basic operation, it lacks a Battery Management System (BMS) , meaning there’s no automatic balancing of charge between the two batteries. As a result, one battery may discharge faster than the other, potentially leading to unstable power delivery or overheating. Despite its drawbacks, this energy solution was chosen because our team lacked the expertise to design and implement a more advanced Li-Po-based system from scratch. It serves as a functional starting point that enables us to focus on software and sensor integration while preparing for future improvements through custom-designed power circuits. 

![LX2-BUSB](https://ndft.com.ua/wp-content/uploads/2024/02/ups18650-9v-1.6a-lx-2bups-01-600x600.jpg)

![mt3068](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRn1Sv7f9wSsHRTk7usT8XIPjlM8y--4sjbYA&s)

---
### Arduino nano
For our autonomous vehicle project, we chose the Arduino Nano with USB-C  as the primary microcontroller to handle sensor inputs, motor control, and coordination with the main Single-Board Computer (SBC), such as a Raspberry Pi. This decision was driven by both practical and ergonomic considerations—primarily, our team’s preference for the USB-C interface , which offers better durability, faster data transfer, and reversible plug orientation compared to older micro-USB connectors. 

While the Arduino Nano (USB-C version) is not strictly required for this project, its compact size, wide community support, and compatibility with the Firmata2 protocol  made it a natural fit for rapid prototyping and integration with Python-based control logic running on the SBC. 
![nano](https://www.universal-solder.ca/wp-content/uploads/2025/01/canaduino-arduino-nano-v3-ch340-USB-C-3.jpg.webp)

---
### L298n
The L298N H-Bridge module  is a dual motor driver commonly used in robotics to control the direction and speed of DC motors. It allows bidirectional motor control using Pulse Width Modulation (PWM) signals from microcontrollers like Arduino or Raspberry Pi. This makes it ideal for basic robotic platforms where simplicity and ease of use are prioritized over high efficiency. 

While the L298N is user-friendly and widely available, it has some limitations such as high voltage drop  (around 1.5V–3V per motor), which reduces the effective voltage delivered to the motors. This can affect performance, especially when using lower-voltage batteries. Additionally, it tends to generate significant heat , often requiring heatsinks or cooling solutions during prolonged operation. We don't opt for more efficient drivers like the DRV8833  or TB6612 , which offer better energy efficiency and thermal performance because find or deliver those drivers for Venezuela is very hard. However, for early development and testing, the L298N remains a solid choice due to its ease of integration and widespread community support.


![L298N](https://http2.mlstatic.com/D_NQ_NP_832041-MLV73442990809_122023-O.webp)

---
## Wiring Diagram
This is the the wiring diagram to assemble your own Dark Halbi! 
Remember to buy every component before start building
![cables](Wiring diagram.png)

At first, we planned to design the car from scratch, modeling and printing our own 3D pieces, including the chassis and direction, Although it seemed like a good idea at first, as we progressed we started to face problem after problem, we realized that our current design would give us more problems, at the end we tried our best with the time constraints we had, and this was the vehicle we presented at WRO 2024, Cybercooper.

![cybercooper](v-photos/old_right.jpg)

### Current Design

#### Prototype

Given the resources we currently had, our main idea was to re-design Cybercooper, modifying the existing base, strategy and using better electronic components; we started printing the new parts with white material and thinking of better ways to assemble the car direction.

#### Fischertechnik kit

At the end, we decided to use a premade base for the chassis, the main reason for this was to save time ( and headaches) with the mechanical design, giving us more time to focus on the electronics and programming.

## Car Photos



# Hardware

## Components


## Mobility

Our vehicle is made the Ackermann steering mechanism, which is a geometric configuration used in vehicle steering systems to ensure that when turning, the inner and outer wheels travel along different radii, preventing tire scrubbing and maximizing cornering stability. This is achieved by steering the front wheels at different angles, with the inner wheel turning at a greater angle than the outer whee

## Power and Sense Management

# Software

We developed the software using python3 as our main programming language and using Thonny/Terminal as code editor.

We wanted to keep the code as simple as possible and use a single language, in order to make this possible we used a library called Pyfirmata which enables us to merge the microcontroller code and the raspberry code in a single unit. 

#### Image Processing

We use the raspberry camera to capture the image, which is converted from BGR format to LAB `(lightness, green-red, blue-yellow)`. We use this colorspace because it's easier to detect the colors, regardless of the environment lighting.

We then use OpenCV to apply a threshold to the image, which returns a mask image with the pixels that reside within the specified color range, we can also reduce processing time by only searching within a specific region of interest on the screen.


###Obstacle Detection

For Obstacle detection, we specify various color ranges that coincide with the color of the obstacles, red and green. After the camera captures the image, we apply gaussian blur and median filters to get a sharper image, the program then applies thresholds to get masks with the colors we are interested in, with this mask we can detected the screen position of the obstacles and the contours of the circuit wall, which can be used to decide the turning direction of the car based on a proportional derivative (PD) algorithm, which involves calculating the differences between the area of the walls

### Open Challenge

#### 

#### Steering Control

### Closed Challenge

#### Obstacle detection
