class UniqueChars(object):
    
    def has_unique_chars(self, string):
        if string is None:
            return False
        
        for char in string:
            if string.count(char):
                return False

        return True
