from functions import * 

# Text Responses (Do wish to pursue surgical speciality)
create_word_document_from_df(df[df['specialty'] == 0], ['Age', 'Gender (1=F, 2=M)', 'Surgical speciality? (0=no, 1=yes)'], ['Why not pursue surgery?', 'What needs to change?'], ['age', 'gender', 'specialty'], ['specialty_reason','specialty_change'], 'responses_no_pursue_surgery.docx')

# Text Response (Do not wish to pursue surgical speciality)
create_word_document_from_df(df[df['specialty'] == 1], ['Age', 'Gender (1=F, 2=M)', 'Surgical speciality? (0=no, 1=yes)'], ['Why pursue surgery?', 'What needs to change?'], ['age', 'gender', 'specialty'], ['specialty_reason','specialty_change'], 'responses_yes_pursue_surgery.docx')
