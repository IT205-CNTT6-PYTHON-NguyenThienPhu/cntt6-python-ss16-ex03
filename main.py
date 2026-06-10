"""
Phần 1:PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP:
1. Phân tích Input/Output của các hàm:
-validate_gender(gender_input: str) -> bool: Nhận vào chuỗi giới tính, trả về True nếu là 'nam' hoặc 'nu', ngược lại False
-find_patient_index(patient_list: list, patient_id: str) -> int: Nhận danh sách và mã BN. Trả về index (int) nếu tìm thấy, không thấy trả về -1
-display_patients(patient_list: list) -> None: Chỉ hiển thị, không trả về dữ liệu
-add_patient(patient_list: list) -> None: Nhận danh sách, tự cập nhật danh sách bên trong hàm
-update_diagnosis(patient_list: list) -> None: Nhận danh sách, tìm kiếm và cập nhật phần tử list con
-search_by_disease(patient_list: list) -> None: Nhận danh sách, in ra kết quả
2. Đề xuất giải pháp & Sự tương tác giữa String và List:
- String: Luôn phải dùng toán tử gán (ví dụ: name = name.strip().title()) vì String là Immutable (Bất biến).
- List: Việc truyền `patient_list` vào các hàm thực chất là truyền Tham chiếu. Khi dùng các phương thức như .append() hay thay đổi trực tiếp list con
"""

# Phần 2.code
def get_non_empty_input(prompt: str, error_msg: str) -> str:
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print(error_msg)
            continue
        return user_input


def validate_gender(gender_input: str) -> bool:
    normalized_gender = gender_input.strip().lower()
    return normalized_gender in ["nam", "nu"]


def find_patient_index(patient_list: list, patient_id: str) -> int:
    normalized_id = patient_id.strip().upper()
    for index, patient in enumerate(patient_list):
        if patient[0] == normalized_id:
            return index
    return -1


def display_patients(patient_list: list) -> None:
    print("----- DANH SÁCH BỆNH NHÂN ĐANG ĐIỀU TRỊ -----")
    if not patient_list:
        print("Hiện không có bệnh nhân nào đang điều trị.")
        return
    for i, patient in enumerate(patient_list, start=1):
        print(f"{i}. Mã: {patient[0]} | Tên: {patient[1]} | Giới tính: {patient[2]} | Bệnh: {patient[3]}")


def add_patient(patient_list: list) -> None:
    print("------ TIẾP NHẬN BỆNH NHÂN MỚI -----")
    while True:
        patient_id = get_non_empty_input("Nhập mã bệnh nhân: ", "Mã bệnh nhân không được để trống!")
        patient_id = patient_id.upper()
        if find_patient_index(patient_list, patient_id) != -1:
            print("Mã bệnh nhân đã tồn tại trong hệ thống, vui lòng kiểm tra lại!")
            continue
        break
    patient_name = get_non_empty_input("Nhập tên bệnh nhân: ", "Tên bệnh nhân không được để trống!")
    patient_name = patient_name.title()

    while True:
        gender = input("Nhập giới tính Nam/Nu: ").strip()
        if validate_gender(gender):
            gender = gender.capitalize()
            break
        print("Giới tính không hợp lệ, vui lòng nhập lại!")
    diagnosis = get_non_empty_input("Nhập chẩn đoán bệnh: ", "Chẩn đoán bệnh không được để trống!")
    diagnosis = diagnosis.capitalize()
    new_patient = [patient_id, patient_name, gender, diagnosis]
    patient_list.append(new_patient)
    print("\nTiếp nhận bệnh nhân thành công!")


def update_diagnosis(patient_list: list) -> None:
    print("\n----- CẬP NHẬT CHẨN ĐOÁN BỆNH -----")
    patient_id = get_non_empty_input("Nhập mã bệnh nhân cần cập nhật: ", "Mã bệnh nhân không được để trống!")
    index = find_patient_index(patient_list, patient_id)
    if index == -1:
        print(f"Không tìm thấy hồ sơ mang mã {patient_id.upper()}!")
        return

    patient = patient_list[index]
    print(f"Tìm thấy bệnh nhân: {patient[1]}")
    print(f"Chẩn đoán hiện tại: {patient[3]}")
    new_diagnosis = get_non_empty_input("Nhập chẩn đoán mới: ", "Chẩn đoán bệnh không được để trống!")
    patient_list[index][3] = new_diagnosis.capitalize()
    print("Cập nhật chẩn đoán bệnh thành công!")

def search_by_disease(patient_list: list) -> None:
    print("----- TÌM KIẾM BỆNH NHÂN THEO TÊN BỆNH -----")
    keyword = get_non_empty_input("Nhập từ khóa tên bệnh: ", "Từ khóa tìm kiếm không được để trống!")
    keyword = keyword.lower()
    found_patients = []
    for patient in patient_list:
        if keyword in patient[3].lower():
            found_patients.append(patient)
    if found_patients:
        print("\nKết quả tìm kiếm:")
        for i, patient in enumerate(found_patients, start=1):
            print(f"{i}. Mã: {patient[0]} | Tên: {patient[1]} | Giới tính: {patient[2]} | Bệnh: {patient[3]}")
    else:
        print("Không tìm thấy bệnh nhân nào phù hợp.")

    print(f"Có tổng cộng {len(found_patients)} bệnh nhân mắc bệnh liên quan đến '{keyword}'.")


def main():
    patients = [
        ["BN001", "Nguyen Van A", "Nam", "Viem Phoi"],
        ["BN002", "Tran Thi B", "Nu", "Sot Xuat Huyet"]
    ]

    while True:
        print("===== HỆ THỐNG QUẢN LÝ BỆNH NHÂN RIKKEI =====")
        print("1. Hiển thị danh sách bệnh nhân")
        print("2. Tiếp nhận bệnh nhân mới")
        print("3. Cập nhật chẩn đoán bệnh theo mã BN")
        print("4. Tìm kiếm và thống kê theo tên bệnh")
        print("5. Thoát chương trình")
        choice = input("Nhập lựa chọn của bạn: ").strip()
        match choice:
            case "1":
                display_patients(patients)
            case "2":
                add_patient(patients)
            case "3":
                update_diagnosis(patients)
            case "4":
                search_by_disease(patients)
            case "5":
                print("Cảm ơn bác sĩ đã sử dụng hệ thống!")
                break
            case _:
                print("Lựa chọn không hợp lệ")
                
if __name__ == "__main__":
    main()