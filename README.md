# DC H-BRIDGE MOTOR DRIVER

Fırçalı DC motorların yön ve hız kontrolü yapmak için en kolay yöntemlerden biri H-BRIDGE devreleridir. MCU'dan gelen PWM sinyalinin değeri sayesinde (HIGH/LOW) mosfetler tetiklenerek motorun bir yönde dönmesini sağlarken, PWM sinyalinin yüksekliği ile motorun hızı kontrol edilir.

Bu kontrol kartında 110A sürekli akım verebilen D2PAK pakete sahip IRF3205 mosfetler ve bu mosfetleri tetiklemek için SOIC8 pakete sahip IR2104S mosfet sürücüler kullanılmıştır. Diğer kondansatör ve direnç gibi komponentler kartın boyutunu küçük tutmak için smd paket seçilmiştir. IR2104S mosfet sürücüler 10-20V besleme gerilimine sahiptir. IRF3205 mosfetler maksimum 55V besleme gerilimine sahiptir fakat devredeki diğer elemanlar maksimum 50V besleme gerilimine daynacak kapasitede kullanılmıştır. Etkili bir soğutma ile bu kontrol kartı ile 40A akıma kadar motor sürmek mümkündür.

PCB çizilirken yüksek akım geçiren devre yolları polygon kullanılarak çizilmiştir. Bu sayede devre yüksek akımda kullanılırken ısı dağılımı daha iyi yapılabilecektir.

IR2104S mosfet sürücülerin Enable durumlarını ve 12V güç giriş durumunu takip edebilmek için PCB üzerine durum ledleri eklenmiştir.

### Resources

IRF3205 Datasheet https://www.infineon.com/dgdl/Infineon-IRF3205S-DataSheet-v01_01-EN.pdf?fileId=5546d462533600a4015355defac9190c

IR2104S Datasheet https://www.infineon.com/dgdl/Infineon-IR2104-DS-v01_00-EN.pdf?fileId=5546d462533600a4015355c7c1c31671

https://www.pcbway.com/blog/technology/Powerful_H_Bridge_DC_Motor_Driver.html


![](https://github.com/mustafasenel/DC_H-BRIDGE_MOTOR_DRIVER/blob/main/front.png)
![](https://github.com/mustafasenel/DC_H-BRIDGE_MOTOR_DRIVER/blob/main/rsz_right.png)                      ![](https://github.com/mustafasenel/DC_H-BRIDGE_MOTOR_DRIVER/blob/main/rsz_left.png)

## SCHEMATIC
![](https://github.com/mustafasenel/DC_H-BRIDGE_MOTOR_DRIVER/blob/main/0001.jpg)
![](https://github.com/mustafasenel/DC_H-BRIDGE_MOTOR_DRIVER/blob/main/0002.jpg)

## PCB PRINT
![](https://github.com/mustafasenel/DC_H-BRIDGE_MOTOR_DRIVER/blob/main/pcb_print.jpg)
![](https://github.com/mustafasenel/DC_H-BRIDGE_MOTOR_DRIVER/blob/main/pcb_frt.png)
![](https://github.com/mustafasenel/DC_H-BRIDGE_MOTOR_DRIVER/blob/main/pcb_front.png)
