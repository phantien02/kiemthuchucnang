def classify_review(review, has_image):
    ## print(len(review))
    if len(review) > 50 and has_image == 1:
            return "nhận xét 5 sao"
    if len(review) < 50 and has_image == 1:
            return "nhận xét 4 sao"
    if has_image == 0:
        return "nhận xét 3 sao"



def test_classify_review():
    # Test cho trường hợp chiều dài là 60 và có ảnh
    result = classify_review("Sản phẩm này thật tuyệt vời! Tôi thực sự ấn tượng với chất lượng và dịch vụ khách hàng. Hãy xem hình ảnh đính kèm để thấy rõ hơn.", True)
    expected = "nhận xét 5 sao"
    assert result == expected, f"Kết quả: {result}, Kỳ vọng: {expected}"

    # Test cho trường hợp chiều dài là 60 và không có ảnh
    result = classify_review( "Sản phẩm này rất tốt và đáng giá tiền. Tôi đã sử dụng nó trong một thời gian và thấy hài lòng. Chỉ tiếc là không có hình ảnh minh họa cho sản phẩm.", False)
    expected = "nhận xét 3 sao"
    assert result == expected, f"Kết quả: {result}, Kỳ vọng: {expected}"

    # Test cho trường hợp chiều dài là 40 và có ảnh
    result = classify_review("Sản phẩm này tốt. Tôi đã chụp một tấm ảnh để bạn thấy nó.", True)
    expected = "nhận xét 5 sao"
    assert result == expected, f"Kết quả: {result}, Kỳ vọng: {expected}"

    # Test cho trường hợp chiều dài là 40 và không có ảnh
    result = classify_review("Sản phẩm ổn định. Không có gì đặc biệt.", True)
    expected = "nhận xét 4 sao"
    assert result == expected, f"Kết quả: {result}, Kỳ vọng: {expected}"

    # Test cho trường hợp chiều dài là 30 và có ảnh
    result = classify_review("Sản phẩm này có tiềm năng, nhưng cần cải thiện ở một số khía cạnh. Tôi hy vọng bạn sẽ nâng cấp nó trong tương lai.", False)
    expected = "nhận xét 3 sao"
    assert result == expected, f"Kết quả: {result}, Kỳ vọng: {expected}"

    # Test cho trường hợp chiều dài là 30 và không có ảnh
    result = classify_review("xấu", False)
    expected = "nhận xét 3 sao"
    assert result == expected, f"Kết quả: {result}, Kỳ vọng: {expected}"

    # Test cho trường hợp khác
    result = classify_review("xấu", True)
    expected = "nhận xét 4 sao"
    assert result == expected, f"Kết quả: {result}, Kỳ vọng: {expected}"

    result = classify_review("", False)
    expected = "nhận xét 3 sao"
    assert result == expected, f"Kết quả: {result}, Kỳ vọng: {expected}"

    print("Tất cả các test cases đã chạy thành công!")


if __name__ == "__main__":
    test_classify_review()
