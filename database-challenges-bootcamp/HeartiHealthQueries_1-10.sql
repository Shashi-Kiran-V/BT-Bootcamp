-- 1. Get all the predictions.

SELECT * 
FROM cardiodiagnosis;

-- 2. Get all the predictions for the day.

SELECT * 
FROM cardiodiagnosis
WHERE DATE(date) = CURRENT_DATE;

SELECT * 
FROM cardiodiagnosis
WHERE DATE(date) = '2019-02-20';

-- 3. Get all the predictions for the day and sort them based on the highest probability percentage at
-- the top.
SELECT * 
FROM cardiodiagnosis
WHERE DATE(date) = '2019-02-20'  
ORDER BY cardioarrestdetected DESC;

-- 4. Get all the unique cities.

SELECT DISTINCT city
FROM addressinfo;

-- 5. Get all the members who are from a city 'Burgos'.

SELECT m.*
FROM memberinfo m
JOIN addressinfo a ON m.member_id = a.memberinfo_member_id
WHERE a.city = 'Burgos';

-- 6. Get all the members who are from 'Flora' city.

SELECT m.*
FROM memberinfo m
JOIN addressinfo a ON m.member_id = a.memberinfo_member_id
WHERE a.city = 'Flora';

-- 7. Get the total number of blood tests done for Aisha.

SELECT COUNT(b.blood_id) AS total_blood_tests
FROM bloodtest b
JOIN cardiodiagnosis c ON b.cardiodiagnosis_cardio_id = c.cardio_id
JOIN memberinfo m ON c.memberinfo_member_id = m.member_id
WHERE m.firstname = 'aisha';

-- 8. Get the X-ray details of Ajay whose cardio test was done on 26th of Jan 2019.

SELECT x.*
FROM xray x
JOIN cardiodiagnosis c ON x.cardiodiagnosis_cardio_id = c.cardio_id
JOIN memberinfo m ON c.memberinfo_member_id = m.member_id
WHERE m.firstname = 'ajay'
  AND DATE(c.date) = '2019-01-26';

-- 9. Get all the members who are from cities 'Burgos' and 'Flora'.
SELECT m.*
FROM memberinfo m
JOIN addressinfo a ON m.member_id = a.memberinfo_member_id
WHERE a.city in ('Burgos', 'Flora');

-- 10. Get the total number of blood tests done for Aberson
SELECT COUNT(b.blood_id) AS total_blood_tests
FROM bloodtest b
JOIN cardiodiagnosis c ON b.cardiodiagnosis_cardio_id = c.cardio_id
JOIN memberinfo m ON c.memberinfo_member_id = m.member_id
WHERE m.firstname = 'aberson';

select * from memberinfo where firstname='aberson';



