import File_management

import urequests

class SendRequest:
    def __init__(self, url, filenameCon, triggerCon, echoCon, echo_timeCon):

        self.url = url
        self.file = File_management.FileManagement(filenameCon,triggerCon, echoCon, echo_timeCon)

    def send(self):
        try:
            data = self.file.getText()
            res = urequests.post(self.url, json={'Distance': [data]})
            print("Server response: ", res.text)
            res.close()
        except Exception as e:
            print("An error occurred while submitting a request: ", e)