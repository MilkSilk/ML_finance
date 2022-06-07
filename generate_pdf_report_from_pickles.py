#%%
import os
import plotly.express as px
import pickle
from fpdf import FPDF


PICKLES_DIRECTORY = 'pickled_results/'
PICKLE_FILES = [
    'initial_modelling.pickle',
    'xgb_scores.pickle',
    'ann_scores.pickle',
    'lstm_scores.pickle'
    ]
pdf = FPDF()


def create_new_page_in_pdf(roi):
    pdf.add_page()
    pdf.set_font("Arial", size = 15)
    pdf.cell(200, 10, txt = f"Target variable: {roi}", ln = 1, align = 'C')


def add_predictor_results(predictor_description, cross_val_description, all_reports_dict, roi, train_test_key, cross_validate_key):
    pdf.set_font("Arial", size = 13)
    pdf.cell(200, 10, txt = predictor_description, ln = 2, align = 'C')
    pdf.set_font("Arial", size = 12)
    pdf.cell(200, 10, txt = "Train-test split (0.67 - 0.33):", ln = 2, align = 'L')
    pdf.set_font("Arial", size = 11)
    for line in all_reports_dict[roi][train_test_key]:
        pdf.cell(200, 10, txt = '        ' + line, ln = 2, align = 'L') 
    
    pdf.set_font("Arial", size = 12)
    pdf.cell(200, 10, txt = cross_val_description, ln = 2, align = 'L')
    pdf.set_font("Arial", size = 11)
    for line in all_reports_dict[roi][cross_validate_key]:
        pdf.cell(200, 10, txt = '        ' + line, ln = 2, align = 'L')

#%%
all_reports_dict = {}
for pickle_file in PICKLE_FILES:
    pickle_path = os.path.join(PICKLES_DIRECTORY, pickle_file)
    with open(pickle_path, 'rb') as f:
        pickle_dict = pickle.load(f)
    if not all_reports_dict:
        all_reports_dict = pickle_dict
    else:
        for roi in all_reports_dict:
            all_reports_dict[roi] = all_reports_dict[roi] | pickle_dict[roi]

# %%
for roi in ['roi_month', 'roi_quarter', 'roi_halfyear', 'roi_year']:
    create_new_page_in_pdf(roi)
    add_predictor_results(
        "Predictor no. 1 - Dummy Regressor (it's prediction is always the mean of the train set)",
        "Cross-validation (split into 10 folds, repeated 3 times):",
        all_reports_dict,
        roi,
        'dummy_train_test',
        'dummy_cross_validate'
    )

    add_predictor_results(
        "Predictor no. 2 - Linear Regression",
        "Cross-validation (split into 10 folds, repeated 3 times):",
        all_reports_dict,
        roi,
        'lin_regr_train_test',
        'lin_regr_cross_validate'
    )

    add_predictor_results(
        "Predictor no. 3 - Gradient Boosting Regressor",
        "Cross-validation (split into 5 folds, repeated 1 time):",
        all_reports_dict,
        roi,
        'xgb_train_test',
        'xgb_cross_validate'
    )

    add_predictor_results(
        "Predictor no. 4 - Multilayer Perceptron",
        "Cross-validation (split into 5 folds, repeated 1 time):",
        all_reports_dict,
        roi,
        'ann_train_test',
        'ann_cross_validate'
    )

    add_predictor_results(
        "Predictor no. 5 - LSTM",
        "Cross-validation (split into 5 folds, repeated 1 time):",
        all_reports_dict,
        roi,
        'lstm_train_test',
        'lstm_cross_validate'
    )

pdf.output('reports/Errors_report.pdf')
# %%
