# Last updated: 7/18/2026, 8:31:31 PM
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 1. Clean and Normalize the Paragraph
        # Replace all non-word characters (including punctuation and spaces) with a single space.
        # This effectively separates words and removes punctuation.
        normalized_paragraph = re.sub(r'[^\w\s]', ' ', paragraph).lower()
        
        # 2. Split and Filter
        # Split the cleaned string into a list of words.
        # Filter out empty strings that may result from extra spaces.
        words = normalized_paragraph.split()
        
        # Convert banned list to a set for O(1) average time complexity lookups
        banned_set = set(banned)
        
        # 3. Count Frequencies of Unbanned Words
        word_counts = Counter()
        max_freq = 0
        most_common = ""
        
        for word in words:
            # Check if the word is NOT in the banned set
            if word not in banned_set:
                word_counts[word] += 1
                current_freq = word_counts[word]
                
                # 4. Track the most common word during the counting process
                if current_freq > max_freq:
                    max_freq = current_freq
                    most_common = word
                    
        return most_common