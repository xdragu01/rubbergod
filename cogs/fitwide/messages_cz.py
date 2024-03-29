from config.messages import Messages as GlobalMessages


class MessagesCZ(GlobalMessages):
    increment_roles_brief = "Aktualizuje role na serveru podle ročníku. Aktualizace školních roomek."
    increment_roles_start = "Incrementing roles..."
    increment_roles_names = "1/3 - Role úspěšně přejmenovány a 0bit a 0mit vytvořen"
    increment_roles_room_names = "2/3 - Kanály úspěšně přejmenovány a 0bit a 0mit general vytvořen"
    increment_roles_success = "3/3 - Holy fuck, všechno se povedlo, tak zase za rok <:Cauec:602052606210211850>"
    role_check_brief = "Zkontroluje ročníkové role uživatelům"
    role_check_start = "Kontrola uživatelů ..."
    role_check_user_not_found = "Ve verified databázi jsem nenašel: {user} ({id})"
    role_check_user_duplicate = "{user} ({id}) je v permit databázi víckrát?"
    role_check_wrong_status = "Status nesedí u: {user} ({id})"
    fitwide_brief = "Příkazy na manipulaci verify studentů"
    update_db_brief = "Aktualizuje databázi s loginy"
    update_db_start = "Aktualizuji databázi..."
    new_logins = "Našel jsem {new_logins} nových loginů."
    update_db_done = "Aktualizace databáze proběhla úspěšně."
    db_debug = "Debug: Našel jsem {cnt_new} nových prvaků."
    pull_db_brief = "Stáhne databázi uživatelů na merlinovi"
    get_db_error = "Při stahování databáze došlo k chybě."
    get_db_timeout = "Timeout při stahování databáze."
    get_db_success = "Stažení databáze proběhlo úspěšně."
    get_login_brief = "Získá xlogin uživatele"
    login_not_found = "Uživatel není v databázi."
    get_user_brief = "Získá discord uživatele"
    get_user_not_found = "Uživatel není v databázi možných loginů."
    get_user_format = "Login: `{p.login}`\nJméno: `{p.name}`\n" "Ročník: `{p.year}`\n"
    invalid_login = "To není validní login."
    action_success = "Příkaz proběhl úspěšně."
    reset_login_brief = "Odstraní uživatele z verify databáze"
    link_login_user_brief = "Propojí login s uživatelem"
    not_in_modroom = "Nothing to see here comrade. <:KKomrade:484470873001164817>"
    login_already_exists = "Uživatel již existuje v databázi."
    vutapi_brief = "Získá data z VUT API"
