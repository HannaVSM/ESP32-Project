
configuration = {
    'sensor_HC-SR04': {
        'TriggerPin': '5',
        'EchoPin': '18',
        'EchoTime': '3000',
    },
    'connection': {
        'Sddi': 'DIOS',
        'Password': 'Daedso24',
    },
    'file': {
        'Filename': 'Data.csv',
    },
    'requests': {
        'Url': 'http://192.168.1.2:3000',
        'Datanumber': '100'
    },
    'bno055':{
        'scl_pin' : '22',
        'sda_pin' : '21'
    }
}