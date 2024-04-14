from functions import * 

# Text Responses (Do wish to pursue surgical speciality)
create_word_document_from_df(df[df['specialty'] == 0], ['Age', 'Gender (1=F, 2=M)', 'Med Year'], ['Why not pursue surgery?', 'What needs to change?'], ['age', 'gender', 'med_year'], ['specialty_reason','specialty_change'], 'responses_no_pursue_surgery.docx')

# Text Response (Do not wish to pursue surgical speciality)
create_word_document_from_df(df[df['specialty'] == 1], ['Age', 'Gender (1=F, 2=M)', 'Med Year'], ['Why pursue surgery?', 'What needs to change?'], ['age', 'gender', 'med_year'], ['specialty_reason','specialty_change'], 'responses_yes_pursue_surgery.docx')

# Surgical Specialty Comments
sx_list = ['orthopaedics', 'general_surgery', 'ob_gyn', 'vascular_surgery', 'urology', 'ent', 'plastic_surgery', 'neurosurgery', 'cardiac_surgery']
create_word_document_from_df(df, ['Age', 'Gender (1=F, 2=M)', 'Med Year'], sx_list, ['age', 'gender', 'med_year'], sx_list, f'specialty_comments.docx')





