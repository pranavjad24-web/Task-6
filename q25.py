class Storage:
    def upload(self):
        pass

class AWS(Storage):
    def upload(self):
        print("Uploaded to AWS")

class GCP(Storage):
    def upload(self):
        print("Uploaded to GCP")

for s in [AWS(), GCP()]:
    s.upload()
