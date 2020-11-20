# message controller

## Instruction to run this project
- Pre-requisite: python and pip should be installed on the machine where this project is expected to run.
- Running the runMessageController.bat for windows or runMessageController.sh for linux will install the required python libraries and then run the application.


## It has two end points
- **POST "/api/create/message"**: you can create new message using this endpoint. The message should be sent in the payload in json format:
    ````
    {
        "title": "great",
        "content": "scot",
        "sender": "puja",
        "url": "http://puja.com"
    }
    ````
  So the ``Content-Type`` should be ``application/json`` 
- **GET "/api/read/messages"**: Read message has two parameters ``version`` and ``format`` . Version ``1`` exclude URL and version ``2`` include URL. Expected formats are ``json`` and ``xml``.
