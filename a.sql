--72. maso, hoten, ten bm, tenql của giaovien tham gia
--tất cả đề tài thuộc chủ đề 'nghiên cứu phát triển'
--kq: giaovien (magv)
--c: detai, chude tencd = nghiên ... (madt)
--bc: thamgiadt
SELECT KQ.MAGV, KQ.HOTEN, (SELECT TENBM FROM BOMON WHERE MABM = KQ.MABM) TENBM,
		(SELECT HOTEN FROM GIAOVIEN QL WHERE QL.MAGV = KQ.GVQLCM)
FROM GIAOVIEN KQ
WHERE NOT EXISTS (SELECT MADT
				FROM DETAI DT JOIN CHUDE CD ON CD.MACD = DT.MACD
				WHERE TENCD = N'NGHIÊN CỨU PHÁT TRIỂN'
				EXCEPT 
				SELECT MADT
				FROM THAMGIADT BC
				WHERE BC.MAGV = KQ.MAGV)
---tập lệnh
--KHAI BÁO BIẾN
DECLARE @MAGV VARCHAR(20), @HOTEN NVARCHAR(30), @NGAYSINH INT
--GÁN GIÁ TRỊ
SET @MAGV = '001'
SET @MAGV = '00' + '1'
SET @MAGV = (SELECT TOP 1 MAGV FROM GIAOVIEN)
SELECT @MAGV = MAGV , @HOTEN = HOTEN, @NGAYSINH = DATEDIFF(YY, NGSINH, GETDATE()) FROM GIAOVIEN
--IN THÔNG BÁO
PRINT @MAGV
PRINT N'MÃ GV LÀ:' + @MAGV
PRINT N'NGÀY SINH:' + CAST(ISNULL(@NGAYSINH,'0') AS VARCHAR(6))

RAISERROR (N'LỖI',16,1)
--CẤU TRÚC RE NHANH
IF (@MAGV = 'DBO')
BEGIN
	PRINT '1'
END
--CẤU TRÚC LẶP
WHILE (@MAGV <> '001')
BEGIN
	
END
GO
-------------thủ tục--------------

IF OBJECT_ID('USP_1') IS NOT NULL  --KIỂM TRA USP_1 TỒN TẠI RỒI
	DROP PROCEDURE USP_1 --XÓA THỦ USP_1
GO
CREATE 
--ALTER
PROC USP_1 
--KHAI BÁO THAM SỐ
	@A INT, --THAM SỐ INPUT
	@B INT,
	@TONG INT OUT --THAM SỐ OUTPUT, CÓ NHIỀU OUTPUT
AS --BÁO KẾT THÚC KHAI BÁO
	--XỬ LÝ
	IF @A < 0 OR @B < 0
	BEGIN
		PRINT 'SAI INPUT'
		RETURN
	END
	RETURN @A + @B
GO --KẾT THÚC THỦ TỤC
DECLARE @K INT,@RT INT
EXEC @RT = USP_1 3,1,@K OUT
PRINT @RT
--YÊU CẦU THÊM GIÁO VIÊN
GO
CREATE
--ALTER
PROC USP_THEMGV
	@MAGV VARCHAR(4),
	@HOTEN NVARCHAR(30),
	@NGAYSINH DATE,
	@MABM NVARCHAR(5)
AS
	IF EXISTS (SELECT * FROM GIAOVIEN WHERE MAGV = @MAGV)
	BEGIN
		PRINT @MAGV + N' ĐÃ TỒN TẠI'
		RETURN
	END
	IF @HOTEN IS NULL OR @NGAYSINH IS NULL
		BEGIN
		PRINT N'DỮ LIỆU KO HL'
		RETURN
	END
	IF NOT EXISTS (SELECT * FROM BOMON WHERE MABM = @MABM)
	BEGIN
		PRINT @MABM + N' KO ĐÃ TỒN TẠI'
		RETURN
	END
	INSERT GIAOVIEN (MAGV,HOTEN, MABM,NGSINH)
	VALUES(@MAGV,@HOTEN,@MABM,@NGAYSINH)
	IF @@ERROR <> 0 
		PRINT 'INSERT KO THÀNH CÔNG'
	ELSE
		PRINT 'INSERT THÀNH CÔNG'
GO
EXEC USP_THEMGV @MAGV = '111',@NGAYSINH='3/3/2000',@MABM = 'MMT',@HOTEN = N'NGUYỄN VẮN B'
SELECT * FROM GIAOVIEN
-----HÀM-----
--GỒM: 2 LOẠI
--LOẠI 1: TRẢ VỀ KIỂU CƠ SỞ (INT, FLOAT, DATE, VARCHAR) -> SỬ DỤNG NHƯ HÀM HỆ THỐNG 
IF OBJECT_ID('UF_1') IS NOT NULL
	DROP FUNCTION UF_1
GO
CREATE FUNCTION UF_1 (@A INT, @B INT)
RETURNS INT --KIỂU CỦA GIÁ TRỊ TRẢ VỀ
AS --KẾT THÚC KHAI BÁO
BEGIN --BẮT BUỘC
	--XỬ LÝ
	--KHÔNG ĐƯỢC DÙNG CÁC LỆNH INSERT, DELETE, UPDATE
	IF @A < 0 OR @B < 0
	BEGIN
		RETURN 0
	END
	RETURN @A + @B
END
GO
PRINT DBO.UF_1(3,4)
--VD: CHO BIẾT GIÁO VIÊN VÀ SỐ ĐỀ TÀI GV THAM GIA
GO
CREATE FUNCTION UF_DEMSODT (@MAGV VARCHAR(5))
RETURNS INT
AS
BEGIN
	RETURN (SELECT COUNT (DISTINCT MADT) FROM THAMGIADT WHERE MAGV = @MAGV)
END
SELECT GV.*, DBO.UF_DEMSODT (MAGV)
FROM GIAOVIEN GV
--LOẠI 2: TRẢ VỀ BẢNG --> DÙNG NHƯ BẢNG
GO
CREATE FUNCTION UF_GIAOVIEN(@MABM NVARCHAR(6))
RETURNS TABLE
AS
	RETURN (SELECT * FROM GIAOVIEN WHERE MABM = @MABM)

SELECT * FROM UF_GIAOVIEN('MMT') A JOIN BOMON BM ON A.MAGV = BM.TRUONGBM
---BÀI TẬP
--viết  function
--1. viết function tính tuổi giáo viên truyền vào MaGV
--2. Viết function đếm số giáo viên mình quản lý truyền vào magv
--3. Viết function tính tổng lương truyền vào mabm
--4. viết function truyền vào mã giáo viên quản lý xuất toàn bộ giáo viên do người này quản lý
--5. viết function truyền madt, stt xuất danh sách magv tham gia đề tài
--6. viết proc thêm tham gia đề tài. Truyền MaGV, MaDT, STT, Phụ cấp.
-----Kiểm tra MaGV tồn tại
-----Kiểm tra CV (madt, stt) tồn tại
-----Kiểm tra giáo viên chưa được phân công cv này
-----Kiểm tra phụ cấp > 0
-----Thêm giáo viên
--7. Viết proc xóa tham gia đề tài của giáo viên. Truyền MaGV, MaDT
-----Kiểm tra MAGV tồn tại
-----Kiểm tra Madt tồn tại
-----Kiểm tra MAGV có được phân cho MaDT
-----Xóa tham gia đề tài
--8. Viết proc cập nhật trưởng BM truyền vào MaBM, TruongBM
-----kiểm tra MaBM tồn tại
-----Kiểm tra trưởng BM tồn tại
-----Kiểm tra trưởng BM có lớn tuổi nhất
-----Cập nhật trưởng BM
--9. Viết proc truyền vào MaGV xuất thông tin MaGV, Hoten, tuổi, số giáo viên quản lý (dùng câu select)	