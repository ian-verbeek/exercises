<<<<<<< HEAD
def word_count(string):
    return len(string.split(" "))

# vraag waarom is ' " " ' nodig? 
# bij test word_count() returnt hij 1 maar er is geen woord
# als ik 'split() gebruik returnt hij 0 wat correcter is
=======
# gemaakt op pc

def word_count(string):
    return len(string.split())

# vraag: waarom is "split(' ')" nodig en niet "split()"
# bij test "word_count()" returnt "split(' ')" 1 maar er is geen woord, "split()" return 0, dit is correcter?
>>>>>>> 6b67f39ea963ddbbb6bfabf70e9c3fbc0dd42244
