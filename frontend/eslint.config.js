import globals from 'globals';
import pluginJs from '@eslint/js';
import tseslint from 'typescript-eslint';
import pluginVue from 'eslint-plugin-vue';


export default [
  {languageOptions: { globals: globals.browser },  rules: {
    'indent': [
      'error', 2
    ],
    '@typescript-eslint/quotes': [
      'error',
      'single',
      {
        'avoidEscape': true,
        'allowTemplateLiterals': true
      },
          
    ]
  }},
  pluginJs.configs.recommended,
  ...tseslint.configs.recommended,
  ...pluginVue.configs['flat/essential'],
];