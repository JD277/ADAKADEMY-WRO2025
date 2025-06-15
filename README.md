## Intro

This is the official Github repository for The Adakademy Team, before known as Adagroup, conformed by Jesser Palma, Jesús Alcalá and Hector Cartagena. This repository contains all the code, documentation, and resources for our project, HALBI. This is our third year participating in WRO
# Team Members
---
* Jesús Alcalá, 20 years old, jdam5000@gmail.com
* Héctor Cartagena, 18 years old, cartagenahector0608@gmail.com
* Jesser Palma, 20 years old, jssrpalma3@gmail.com
*  
# 📖 Content of README 📖
* **[Hardware](#-hardware-)**
  * [Components](#%EF%B8%8F-components-%EF%B8%8F)
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
# Hardware
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
| 2        | [LX-2BUPS](https://www.amazon.com/-/es/Bater%C3%ADa-M%C3%B3dulo-Cargador-Tablero-Indicador/dp/B0CGZS38QR/ref=sr_1_1?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=136Q8NU91WK25&dib=eyJ2IjoiMSJ9.OUZ7CB2S6RhhunyygWStlhYXdkOxEQWEOd7igJQg-ILCCJFEW-Is87jcLbWIrBYqBUWPaTZceymcS13W2cNtIA.zeXlgUhXAuX3iUN4TpHTLoBrpBR5GAd59arz0m_-F44&dib_tag=se&keywords=lx-2bups&qid=1749991945&sprefix=lx-2bups%2Caps%2C289&sr=8-1&th=1)               | $5.24          | $10.48 |
| 2        | [USB cable type C](https://www.amazon.com/paquete-cables-trenzados-iPhone-Samsung/dp/B0DPMQ7291/ref=sr_1_2_sspa?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=19WFOH9SGQR6X&dib=eyJ2IjoiMSJ9.TwlOm7HeKVsOKER2sTeYNLD5mWAyTg5X856GRR8FkQvdG6_mf3AkJUFATBnv2BeM8xp9pvV-C07pI8XJwoQ_eKhFW_LFDsdW4gMXxY4SR16LNgk9hBwUKvpjZFP6bFsEPKocQuodZaAIRYU69ZSXUM4tDsU4ICjfgal6OKZ0AduJXFmkanzaBUevDxYOerGFGKB3YJBU--yu-UaFZyqTN1Tva5bVN1G6vEmKS4970rU.FvhJ8ACjur6SL9B8e6yG-afZRtFQW6M1iDPJC9vrJN0&dib_tag=se&keywords=usb%2Bcable%2BC&qid=1749992275&sprefix=usb%2Bcable%2Bc%2Caps%2C204&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1)       | $6.00          | $12.00 |
| **Total** |                        |                | **$460.48** |
### First Design

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
