import sys

class TrieNode():
    def __init__(self):
        self.children = {}
        self.word = None

def build_trie(word_scores):
    root = TrieNode()

    for word in word_scores:
        current = root

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()

            current = current.children[char]

        # This node is the end of this complete word.
        current.word = word

    return root


def find_words(text, start, root):
    """
    Find all dictionary words that start at text[start].

    Yield:
        (end_position, word)
    """
    current = root

    for end in range(start, len(text)):
        char = text[end]

        # No matching next character:
        # no longer word can match either.
        if char not in current.children:
            break

        current = current.children[char]

        # Found a complete dictionary word.
        if current.word is not None:
            yield end + 1, current.word



def main():
    data = sys.stdin.readline
    text = data()
    n = int(data())

    scores = {}
    for _ in range(n):
        word, score = list(data().split())
        score = int(score)
        scores[word] = score

    m = int(data())
    transition_scores = {}
    for _ in range(m):
        word1, word2, score = list(data().split())
        score = int(score)
        transition_scores[(word1, word2)] = score

    root = build_trie(scores)
    text_length = len(text)

    #dp[position] = {last_words:best_score}
    dp = [{} for _ in range(text_length + 1)]
    dp[0] = None

    for start in range(text_length + 1):
        if not dp[start]:
            continue

        matched_words = list(find_words(text, start, root))

        for end, current_word in matched_words:
            word_score = scores[current_word]

            for previous_word, old_score in dp[start].items():
                t_score = transition_scores.get((previous_word, current_word), 0)

                new_score = old_score + word_score + t_score

                old_best = dp[end].get(current_word)

                if old_best is None or new_score > old_best:
                    dp[end][current_word] = new_score

    if not dp[text_length]: 
        print(0)
        return

    print(max(dp[text_length].values()))



if __name__ == "__main__":
    main()