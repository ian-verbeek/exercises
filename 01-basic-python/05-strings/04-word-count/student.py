def word_count(string):
    return len(string.split(" "))

# vraag waarom is ' " " ' nodig? 
# bij test word_count() returnt hij 1 maar er is geen woord
# als ik 'split() gebruik returnt hij 0 wat correcter is
