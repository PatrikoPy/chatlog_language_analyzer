import datetime


class Entry:

    def __init__(self, *args):
        self.__datetime, self.__author, self.__content, self.__channel, self.__lang = args
        self.__converted_datetime = datetime.datetime.today()

    def get_content(self):
        return self.__content

    def get_author(self):
        return self.__author

    def convert_datetime(self):
        pass

    def get_datetime(self):
        return self.__converted_datetime.strftime('%d %B %H:%M:%S.%f')

    def get_channel(self):
        return self.__channel

    def get_lang(self):
        return self.__lang


class EntryWow(Entry):
    def __init__(self, *args):
        super().__init__(*args)
        self.__datetime, self.__author, self.__content, self.__channel, self.__lang = args
        self.__converteddatetime = self.convert_datetime()

    def convert_datetime(self):
        dt = datetime.datetime.strptime(self.__datetime, '%m/%d %H:%M:%S.%f')
        return dt

    def __str__(self):
        return f"Log entry from WoW:\n{self.__datetime} | from: {self.__author} | content: {self.__content}"


class EntryFortnite(Entry):

    def __init__(self, *args):
        super().__init__(*args)
        self.__datetime, self.__author, self.__content, self.__channel, self.__lang = args
        self.__converteddatetime = self.convert_datetime()

    def convert_datetime(self):
        dt = datetime.datetime.strptime(self.__datetime, '%Y-%m-%d %H:%M:%S.%f')
        return dt

    def __str__(self):
        return f"Log entry from Fortnite:\n{self.__datetime} | from: {self.__author} | content: {self.__content}"
