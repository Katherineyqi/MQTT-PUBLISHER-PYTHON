import paho.mqtt.client as mqtt # Mqtt library
import thread # hello
import time
temp='0'
level1='1' 
level2='2'

def ante_conexion_exitosa(client, userdata, flags, rc):
    print("Conectados con exito")
    client.subscribe("3EyLfoLCMSY8seG/nivel1")
    client.subscribe("3EyLfoLCMSY8seG/nivel22")
    client.subscribe("3EyLfoLCMSY8seG/temperatura")
    client.publish("3EyLfoLCMSY8seG/nivel1","level1")
    client.publish("3EyLfoLCMSY8seG/nivel2","level2")
    client.publish("3EyLfoLCMSY8seG/temperatura","temp")
   
def ante_llegada_mensaje(client, userdata, msg):
    print("llego dato")
    print(msg.payload.decode("utf-8"))

cliente=mqtt.Client()
cliente.on_connect=ante_conexion_exitosa
cliente.on_message=ante_llegada_mensaje

cliente.username_pw_set("pKGeOCpyFia9Dhy","5bJSp0QQKGvuIWM")
cliente.connect("ioticos.org",1883,60)

while True:
    time.sleep(5)

    a_enviar= temp
    b_enviar= level1
    c_enviar= level2
    cliente.publish("3EyLfoLCMSY8seG/temperatura",a_enviar)
    cliente.publish("3EyLfoLCMSY8seG/nivel1",b_enviar)
    cliente.publish("3EyLfoLCMSY8seG/nivel2",c_enviar)
    cliente.loop()
    
