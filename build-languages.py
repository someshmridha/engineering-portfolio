from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
reference = json.loads((ROOT / 'content-reference.json').read_text(encoding='utf-8'))
required = set(reference['translations']['en']) | set(reference['portfolioEvidence']['labels']['en']) | {'navEducation'}
locales = {}
for code in ('hi', 'bn', 'ta', 'sa'):
    path = ROOT / 'translations' / f'{code}.json'
    text = path.read_text(encoding='utf-8')
    if code == 'hi':
        text = text.replace('अंतरिक्ष-सदिश', 'स्पेस-वेक्टर')
    elif code == 'bn':
        text = text.replace('MMSE সমীকরণ', 'MMSE ইকুয়ালাইজেশন').replace('সমীকরণের জন্য', 'ইকুয়ালাইজেশনের জন্য')
    elif code == 'sa':
        text = text.replace('मध्यः', 'माध्यः').replace('MMSE-समीकरणम्', 'MMSE-समताकरणम्').replace('समीकरणाय', 'समताकरणाय')
    path.write_text(text, encoding='utf-8')
    locale = json.loads(text)
    assert not required - set(locale['labels']), (code, sorted(required - set(locale['labels'])))
    assert all(isinstance(v, str) and v.strip() for v in locale['labels'].values()), code
    for case_id, old in reference['cases'].items():
        case = locale['cases'][case_id]
        assert set(case) == set(old['en']), (code, case_id, 'case fields')
        for key, value in case.items():
            assert isinstance(value, (str, list)) and value, (code, case_id, key)
            if isinstance(value, list):
                assert len(value) == len(old['en'][key]), (code, case_id, key)
                assert all(isinstance(v, str) and v.strip() for v in value)
        for group in ('parameters', 'decisions', 'galleries'):
            expected = reference['portfolioEvidence'][group][case_id]
            expected_count = len(expected) if group == 'galleries' else len(expected['en'])
            values = locale[group][case_id]
            assert len(values) == expected_count, (code, group, case_id)
            assert all(len(row) == (3 if group == 'galleries' else 2) for row in values)
            assert all(isinstance(s, str) and s.strip() for row in values for s in row)
    assert all(v in locale['cases']['research']['evidence'] for v in ('19.34%', '29.26%', '0 dB'))
    assert all(v in locale['cases']['energy']['evidence'] for v in ('58 V', '50 W', '46.4 W', '92.8%'))
    assert '3.71/4.00' in locale['labels']['currentGpa']
    assert '7.75/10.00' in locale['labels']['finalCgpa']
    assert all(token in locale['labels']['chartReading'] for token in ('{channel}', '{ls}', '{wls}'))
    locales[code] = locale

(ROOT / 'dist' / 'languages.js').write_text(
    "'use strict';\nconst additionalLanguages=" + json.dumps(locales, ensure_ascii=False, separators=(',', ':')) + ';\n',
    encoding='utf-8'
)
print(json.dumps({'new_languages': list(locales), 'translated_labels_per_language': len(locales['hi']['labels']), 'cases_per_language': 3, 'original_figures_per_language': 13, 'checks': 'passed'}))
