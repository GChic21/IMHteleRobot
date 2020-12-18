# En este bloque se define la parada si el arduino
# detecta el borde de la mesa

def on_microbit_id_io_p2_pin_evt_rise():
    gigglebot.stop()
control.on_event(EventBusSource.MICROBIT_ID_IO_P2,
    EventBusValue.MICROBIT_PIN_EVT_RISE,
    on_microbit_id_io_p2_pin_evt_rise)

# En este bloque final se define el movimiento
# para los eventos de pulsación de los botones en la app

def on_mes_dpad_controller_id_button_c_down():
    gigglebot.turn_millisec(gigglebotWhichTurnDirection.RIGHT, 1000)
control.on_event(EventBusSource.MES_DPAD_CONTROLLER_ID,
    EventBusValue.MES_DPAD_BUTTON_C_DOWN,
    on_mes_dpad_controller_id_button_c_down)

# Definimos unas imágenes a mostrar en los led
# cuando el bluetooth esté o no conectado

def on_bluetooth_connected():
    images.icon_image(IconNames.YES).show_image(0)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    images.icon_image(IconNames.NO).show_image(0)
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def on_mes_dpad_controller_id_button_d_down():
    gigglebot.turn_millisec(gigglebotWhichTurnDirection.RIGHT, 1000)
control.on_event(EventBusSource.MES_DPAD_CONTROLLER_ID,
    EventBusValue.MES_DPAD_BUTTON_D_DOWN,
    on_mes_dpad_controller_id_button_d_down)

def on_mes_dpad_controller_id_button_b_down():
    gigglebot.drive_straight(gigglebotWhichDriveDirection.BACKWARD)
control.on_event(EventBusSource.MES_DPAD_CONTROLLER_ID,
    EventBusValue.MES_DPAD_BUTTON_B_DOWN,
    on_mes_dpad_controller_id_button_b_down)

def on_mes_dpad_controller_id_button_a_down():
    gigglebot.drive_straight(gigglebotWhichDriveDirection.FORWARD)
control.on_event(EventBusSource.MES_DPAD_CONTROLLER_ID,
    EventBusValue.MES_DPAD_BUTTON_A_DOWN,
    on_mes_dpad_controller_id_button_a_down)

def on_mes_dpad_controller_id_button_b_up():
    gigglebot.stop()
control.on_event(EventBusSource.MES_DPAD_CONTROLLER_ID,
    EventBusValue.MES_DPAD_BUTTON_B_UP,
    on_mes_dpad_controller_id_button_b_up)

def on_mes_dpad_controller_id_button_d_up():
    gigglebot.stop()
control.on_event(EventBusSource.MES_DPAD_CONTROLLER_ID,
    EventBusValue.MES_DPAD_BUTTON_D_UP,
    on_mes_dpad_controller_id_button_d_up)

def on_mes_dpad_controller_id_button_c_up():
    gigglebot.stop()
control.on_event(EventBusSource.MES_DPAD_CONTROLLER_ID,
    EventBusValue.MES_DPAD_BUTTON_C_UP,
    on_mes_dpad_controller_id_button_c_up)

def on_mes_dpad_controller_id_button_a_up():
    gigglebot.stop()
control.on_event(EventBusSource.MES_DPAD_CONTROLLER_ID,
    EventBusValue.MES_DPAD_BUTTON_A_UP,
    on_mes_dpad_controller_id_button_a_up)
