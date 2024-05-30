import os

translations = {
    "en_US": {
        "sneakyLabel": "Focus mode",
        "enable": "Enable",
        "disable": "Disable",
        "quit": "Quit"
    },
    "fr_FR": {
        "sneakyLabel": "Mode concentration",
        "enable": "Activer",
        "disable": "Désactiver",
        "quit": "Quitter"
    },
    "de_DE": {
        "sneakyLabel": "Fokusmodus",
        "enable": "Aktivieren",
        "disable": "Deaktivieren",
        "quit": "Beenden"
    },
    "fr_BE": {
        "sneakyLabel": "Mode concentration",
        "enable": "Activer",
        "disable": "Désactiver",
        "quit": "Quitter"
    },
    "ru_RU": {
        "sneakyLabel": "Режим фокуса",
        "enable": "Включить",
        "disable": "Отключить",
        "quit": "Выйти"
    },
    "it_IT": {
        "sneakyLabel": "Modalità concentrazione",
        "enable": "Abilita",
        "disable": "Disabilita",
        "quit": "Esci"
    },
    "en_GB": {
        "sneakyLabel": "Focus mode",
        "enable": "Enable",
        "disable": "Disable",
        "quit": "Quit"
    },
    "es_ES": {
        "sneakyLabel": "Modo enfoque",
        "enable": "Habilitar",
        "disable": "Deshabilitar",
        "quit": "Salir"
    },
    "pt_PT": {
        "sneakyLabel": "Modo de foco",
        "enable": "Ativar",
        "disable": "Desativar",
        "quit": "Sair"
    },
    "hr_HR": {
        "sneakyLabel": "Način fokusiranja",
        "enable": "Omogući",
        "disable": "Onemogući",
        "quit": "Izađi"
    },
    "sr_RS": {
        "sneakyLabel": "Режим фокуса",
        "enable": "Омогући",
        "disable": "Онемогући",
        "quit": "Излаз"
    },
    "tr_TR": {
        "sneakyLabel": "Odak modu",
        "enable": "Etkinleştir",
        "disable": "Devre dışı bırak",
        "quit": "Çık"
    },
    "he_IL": {
        "sneakyLabel": "מצב מיקוד",
        "enable": "הפעל",
        "disable": "השבת",
        "quit": "צא"
    },
    "ar_SA": {
        "sneakyLabel": "وضع التركيز",
        "enable": "تفعيل",
        "disable": "تعطيل",
        "quit": "إنهاء"
    },
    "ar_MA": {
        "sneakyLabel": "وضع التركيز",
        "enable": "تفعيل",
        "disable": "تعطيل",
        "quit": "إنهاء"
    },
    "ar_TN": {
        "sneakyLabel": "وضع التركيز",
        "enable": "تفعيل",
        "disable": "تعطيل",
        "quit": "إنهاء"
    },
    "ar_DZ": {
        "sneakyLabel": "وضع التركيز",
        "enable": "تفعيل",
        "disable": "تعطيل",
        "quit": "إنهاء"
    },
    "ar_LY": {
        "sneakyLabel": "وضع التركيز",
        "enable": "تفعيل",
        "disable": "تعطيل",
        "quit": "إنهاء"
    },
    "hi_IN": {
        "sneakyLabel": "फ़ोकस मोड",
        "enable": "सक्षम करें",
        "disable": "अक्षम करें",
        "quit": "बाहर निकलें"
    },
    "zh_CN": {
        "sneakyLabel": "专注模式",
        "enable": "启用",
        "disable": "禁用",
        "quit": "退出"
    },
    "ja_JP": {
        "sneakyLabel": "フォーカスモード",
        "enable": "有効にする",
        "disable": "無効にする",
        "quit": "終了"
    },
    "nl_NL": {
        "sneakyLabel": "Focusmodus",
        "enable": "Inschakelen",
        "disable": "Uitschakelen",
        "quit": "Afsluiten"
    },
    "sv_SE": {
        "sneakyLabel": "Fokusläge",
        "enable": "Aktivera",
        "disable": "Inaktivera",
        "quit": "Avsluta"
    },
    "da_DK": {
        "sneakyLabel": "Fokusindstilling",
        "enable": "Aktiver",
        "disable": "Deaktiver",
        "quit": "Afslut"
    },
    "no_NO": {
        "sneakyLabel": "Fokusmodus",
        "enable": "Aktiver",
        "disable": "Deaktiver",
        "quit": "Avslutt"
    },
    "fi_FI": {
        "sneakyLabel": "Keskitystila",
        "enable": "Ota käyttöön",
        "disable": "Poista käytöstä",
        "quit": "Lopeta"
    },
    "pl_PL": {
        "sneakyLabel": "Tryb skupienia",
        "enable": "Włącz",
        "disable": "Wyłącz",
        "quit": "Zakończ"
    },
    "cs_CZ": {
        "sneakyLabel": "Režim soustředění",
        "enable": "Povolit",
        "disable": "Zakázat",
        "quit": "Ukončit"
    },
    "ko_KR": {
        "sneakyLabel": "집중 모드",
        "enable": "활성화",
        "disable": "비활성화",
        "quit": "종료"
    },
    "el_GR": {
        "sneakyLabel": "Λειτουργία εστίασης",
        "enable": "Ενεργοποίηση",
        "disable": "Απενεργοποίηση",
        "quit": "Έξοδος"
    },
    "hu_HU": {
        "sneakyLabel": "Fókusz mód",
        "enable": "Engedélyez",
        "disable": "Letilt",
        "quit": "Kilépés"
    },
    "ro_RO": {
        "sneakyLabel": "Mod de concentrare",
        "enable": "Activează",
        "disable": "Dezactivează",
        "quit": "Ieșire"
    },
    "sk_SK": {
        "sneakyLabel": "Režim sústredenia",
        "enable": "Povoliť",
        "disable": "Zakázať",
        "quit": "Ukončiť"
    },
    "th_TH": {
        "sneakyLabel": "โหมดโฟกัส",
        "enable": "เปิดใช้งาน",
        "disable": "ปิดใช้งาน",
        "quit": "ออก"
    },
    "vi_VN": {
        "sneakyLabel": "Chế độ tập trung",
        "enable": "Kích hoạt",
        "disable": "Vô hiệu hóa",
        "quit": "Thoát"
    },
    "bn_BD": {
        "sneakyLabel": "ফোকাস মোড",
        "enable": "সক্রিয় করুন",
        "disable": "নিষ্ক্রিয় করুন",
        "quit": "প্রস্থান করুন"
    },
    "fa_IR": {
        "sneakyLabel": "حالت تمرکز",
        "enable": "فعال سازی",
        "disable": "غیرفعال سازی",
        "quit": "خروج"
    },
    "uk_UA": {
        "sneakyLabel": "Режим фокусування",
        "enable": "Активувати",
        "disable": "Деактивувати",
        "quit": "Вийти"
    }
}


def i18n(text):
    locale = os.getenv('LANG', 'en_US').split('.')[0]
    locale_translations = translations.get(locale, {})
    return locale_translations.get(text, text)


