from aiogram_i18n.cores import FluentRuntimeCore
from aiogram_i18n.middleware import I18nMiddleware

i18n_middleware = I18nMiddleware(
    FluentRuntimeCore(path='bot/locales', default_locale='en')
)

middlewares_list = [i18n_middleware]
