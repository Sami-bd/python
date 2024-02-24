class Solution:
    def reverseVowels(self, s: str) -> str:
        def remove_vowels_and_store_separate_arrays(input_string):
            vowels = "aeiouAEIOU"
            result = ''.join(char for char in input_string if char not in vowels)
            vowel_indices = [index for index, char in enumerate(input_string) if char in vowels]
            removed_vowels = [char for char in input_string if char in vowels]
            return result, vowel_indices, removed_vowels

        # Example usage:
        
        output_string, vowel_indices, removed_vowels = remove_vowels_and_store_separate_arrays(s)


        str_list = [char for char in output_string]
        for item1, item2 in zip(vowel_indices, reversed(removed_vowels)):
            str_list.insert(item1, item2)

        finalResult = ''.join(char for char in str_list)


        return finalResult

