
import time

from typing import List
from src.processing.constants import ACCEPTED_LANGUAGES
from src.processing.coh_metrix_indices.descriptive_indices import DescriptiveIndices
from src.processing.coh_metrix_indices.syntactic_pattern_density_indices import SyntacticPatternDensityIndices
from src.processing.coh_metrix_indices.word_information_indices import WordInformationIndices
from src.processing.coh_metrix_indices.syntactic_complexity_indices import SyntacticComplexityIndices


class TextComplexityAnalizer:
    '''
    This class groups all of the indices in order to calculate them in one go. It works for a specific language.
    '''
    def __init__(self, language:str = 'es') -> None:
        '''
        This constructor initializes the analizer for a specific language.

        Parameters:
        language(str): The language that the texts are in.

        Returns:
        None.
        '''
        if not language in ACCEPTED_LANGUAGES:
            raise ValueError(f'Language {language} is not supported yet')

        self._di = DescriptiveIndices(language)
        self._spdi = SyntacticPatternDensityIndices(language)
        self._wii = WordInformationIndices(language)
        self._sci = SyntacticComplexityIndices(language)

    def analize_texts(self, files: List[str]) -> List:
        '''
        This method will calculate all the metrics for a group of files.

        Parameters:
        files(List[str]): A list of the absolute paths to the files to analize.

        Returns:
        List: The indices calculated for each file.
        '''
        try:
            results = []

            for filepath in files: # For each file
                with open(filepath, 'r') as f:
                    text = f.read()
                    start = time.time()
                    results.append([self._spdi.get_noun_phrase_density(text=text),
                                    self._spdi.get_verb_phrase_density(text=text),
                                    self._spdi.get_negative_expressions_density(text=text),
                                    self._wii.get_verb_count(text=text),
                                    self._wii.get_noun_count(text=text),
                                    self._wii.get_adjective_count(text=text),
                                    self._wii.get_adverb_count(text=text),
                                    self._wii.get_personal_pronoun_count(text=text),
                                    self._wii.get_personal_pronoun_first_person_single_form_count(text=text),
                                    self._wii.get_personal_pronoun_first_person_plural_form_count(text=text),
                                    self._wii.get_personal_pronoun_second_person_single_form_count(text=text),
                                    self._wii.get_personal_pronoun_second_person_plural_form_count(text=text),
                                    self._wii.get_personal_pronoun_third_person_singular_form_count(text=text),
                                    self._wii.get_personal_pronoun_third_person_plural_form_count(text=text),
                                    self._di.get_paragraph_count_from_text(text=text),
                                    self._di.get_sentence_count_from_text(text=text),
                                    self._di.get_word_count_from_text(text=text),
                                    self._di.get_mean_of_length_of_paragraphs(text=text),
                                    self._di.get_std_of_length_of_paragraphs(text=text),
                                    self._di.get_mean_of_length_of_sentences(text=text),
                                    self._di.get_std_of_length_of_sentences(text=text),
                                    self._di.get_mean_of_length_of_words(text=text),
                                    self._di.get_std_of_length_of_words(text=text),
                                    self._di.get_mean_of_syllables_per_word(text=text),
                                    self._di.get_std_of_syllables_per_word(text=text),
                                    self._sci.get_mean_number_of_modifiers_per_noun_phrase(text=text)])
                    end = time.time()           
                    print(f'Tiempo demorado para este texto: {end - start} segundos.')

            return results
        except Exception as e:
            raise e