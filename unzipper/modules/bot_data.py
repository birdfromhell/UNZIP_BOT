# Copyright (c) 2021 Itz-fork
# Don't kang this else your dad is gae

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Inline buttons
class Buttons:
    START_BUTTON = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("Help 📜", callback_data="helpcallback"),
                InlineKeyboardButton("About ⁉️", callback_data="aboutcallback")
            ]
        ])
    
    CHOOSE_E_F__BTNS = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("File Extract 📂", callback_data="extract_file|tg_file|no_pass"),
            ],
            [
                InlineKeyboardButton("File (Password) Extract 📂", callback_data="extract_file|tg_file|with_pass")
            ],
            [
                InlineKeyboardButton("Batal ❌", callback_data="cancel_dis")
            ]
        ])

    CHOOSE_E_U__BTNS = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("🔗 Url Extract 📂", callback_data="extract_file|url|no_pass"),
            ],
            [
                InlineKeyboardButton("🔗 (Password) Url Extract 📂", callback_data="extract_file|url|with_pass")
            ],
            [
                InlineKeyboardButton("Batal ❌", callback_data="cancel_dis")
            ]
        ])

    CLN_BTNS = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("Clean My Files 😇", callback_data="cancel_dis")
            ],
            [
                InlineKeyboardButton("TF! Nooo 😳", callback_data="nobully")
            ]
        ])
    
    ME_GOIN_HOME = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("Kembali 🏡", callback_data="megoinhome")
            ]
        ])

    SET_UPLOAD_MODE_BUTTONS = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("Sebagai Doc 📁", callback_data="set_mode|doc")
            ],
            [
                InlineKeyboardButton("Sebagai Video 📹", callback_data="set_mode|video")
            ]
        ])


class Messages:
    START_TEXT = """
Hi **{}**, I'm **Unzipper Bot** 😇!

`Saya Bisa Mengextract archives Seperti zip, rar, tar etc.`

**Made with ❤️ by @MustaxProject**
    """

    HELP_TXT = """
**Bagaimana cara Mengextract Extract? 🤔**

`1. Kirim File Atau Link Yang Akan Di Extract.`
`2. Klik Tombol extract(Jika kamu Menggunakan URL Klik Tombol "Url Extract". Jika Ini File Gunakan Tombol "File Extract").`

**Bagaimana Mengganti Mode Upload ? 🤔**
 `Kirim` Perintah **/mode** ` Ke Bot. Anda dapat mengubah mode Upload Disana.`

**Note:**
    **1.** `Jika arsip Anda dilindungi kata sandi, pilih` **(Password) Extract 📂** `mode. Bot bukan TUHAN yang mengetahui kata sandi file Anda, jadi Jika ini terjadi, kirimkan saja kata sandi itu!`
    
    **2.** `Jangan Kirim File Yang corrupted! Jika Anda mengirim satu karena kesalahan, kirim saja Perintah` **/clean**!`
    
    **3.** `Jika arsip Anda memiliki 95 atau lebih file di dalamnya, bot tidak dapat menampilkan semua file yang diekstraksi untuk dipilih. Jadi jika Anda tidak dapat melihat file Anda di tombol, cukup klik tombol` "Unggah Semua ♻️" `. Ini akan mengirim semua file yang diekstraksi kepada Anda!`
    """

    ABOUT_TXT = """
**About Unzipper Bot,**

✘ **Language:** [Python](https://www.python.org/)
✘ **Framework:** [Pyrogram](https://docs.pyrogram.org/)
✘ **Source Code:** [Contact-Me](https://t.me/BIRD_from_HELL)
✘ **Developer:** [BirdFromHell](https://t.me/BIRD_from_HELL)


**Made with ❤️ by @MustaxProject**
    """

    LOG_TXT = """
**Extract Log 📝!**

**User ID:** `{}`
**File Name:** `{}`
**File Size:** `{}`
    """

    AFTER_OK_DL_TXT = """
**Successfully Downloaded**

**Download time:** `{}`
**Status:** `Mencoba Mengextract File`
    """

    EXT_OK_TXT = """
**Extraction Successfull!**

**Extraction time:** `{}`
**Status:** `Mencoba Mengupload`
    """

    EXT_FAILED_TXT = """
**Extraction Gagal 😕!**

**What to do?**

 - `Pastikan arsip tidak rusak`
 - `Pastikan Kamu memilih mode yang tepat!`
 - `Mungkin format arsip Anda tidak didukung 😔`

**Silahkan Lapor Ke @BIRD_from_HELL Jika Bot Terjadi Error**
    """

    ERROR_TXT = """
**Terjadi kesalahan 😕!**

**ERROR:** {}


**Please report this at @Nexa_bots if you think this is a serious error**
    """

    CANCELLED_TXT = """
**{} ✅!**

`Now all of your files have been deleted from my server 😏!`
    """

    CLEAN_TXT = """
**Are sure want to delete your files from my server 🤔?**

**Note:** `This action cannot be undone!`
    """

    SELECT_UPLOAD_MODE_TXT = """
`Please select the upload mode by clicking on below buttons!`

**Current Upload mode is:** `{}`
"""
    CHANGED_UPLOAD_MODE_TXT = """
**Successfully changed upload mode to** `{}` **✅!**
"""


# List of error messages from p7zip
ERROR_MSGS = [
    "Error",
    "Can't open as archive"
    ]