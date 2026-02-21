class TrieNode:
    __slots__ = ("children", "top5")

    def __init__(self):
        self.children = {}
        # top5 stores tuples: (frequency, word)
        # Always sorted descending by frequency
        self.top5 = []


class AutocompleteSystem:
    def __init__(self):
        self.root = TrieNode()
        self.word_freq = {}   # global frequency table

    # Insert a word into Trie
    def insert(self, word: str):
        # Update global frequency
        self.word_freq[word] = self.word_freq.get(word, 0) + 1
        freq = self.word_freq[word]

        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()

            node = node.children[ch]
            self._update_top5(node, word, freq)

    # Maintain top 5 list at each node
    def _update_top5(self, node: TrieNode, word: str, freq: int):
        # Remove existing entry if present
        node.top5 = [(f, w) for f, w in node.top5 if w != word]

        # Add updated value
        node.top5.append((freq, word))

        # Sort by frequency desc, then lexicographically
        node.top5.sort(key=lambda x: (-x[0], x[1]))

        # Keep only top 5
        if len(node.top5) > 5:
            node.top5.pop()

    # Prefix search: O(L)
    def search(self, prefix: str):
        node = self.root

        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]

        # Return only words
        return [word for _, word in node.top5]

if __name__ == "__main__":
    ac = AutocompleteSystem()

    words = [
        "apple", "app", "application", "ape", "april",
        "apple", "app", "apple", "apply", "app"
    ]

    for w in words:
        ac.insert(w)

    print(ac.search("a"))    # Top 5 for prefix "ap"
    print(ac.search("app"))   # Top 5 for prefix "app"