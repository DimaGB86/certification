'''Задание 1. Логирование с использованием нескольких файлов
Напишите скрипт, который логирует разные типы сообщений в разные файлы.
Логи уровня DEBUG и INFO должны сохраняться в debug_info.log, а логи уровня
WARNING и выше — в warnings_errors.log.
'''

import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

debug_info_handler = logging.FileHandler('debug_info.log', encoding='utf-8', mode='w')
debug_info_handler.setLevel(logging.DEBUG)
debug_info_handler.setFormatter(formatter)
logger.addHandler(debug_info_handler)

warnings_errors_handler = logging.FileHandler('warnings_errors.log', encoding='utf-8', mode='w')
warnings_errors_handler.setLevel(logging.WARNING)
warnings_errors_handler.setFormatter(formatter)
logger.addHandler(warnings_errors_handler)

logging.debug('Уровень: DEBUG')
logging.info('Уровень: INFO')
logging.warning('Уровень: WARNING')
logging.error('Уровень: ERROR')
logging.critical('Уровень: CRITICAL')


