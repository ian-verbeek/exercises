# gemaakt op pc

def word_count(string):
    return len(string.split())

# vraag: waarom is "split(' ')" nodig en niet "split()"
# bij test "word_count()" returnt "split(' ')" 1 maar er is geen woord, "split()" return 0, dit is correcter?