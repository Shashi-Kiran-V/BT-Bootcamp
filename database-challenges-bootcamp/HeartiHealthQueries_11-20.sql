-- 11. Get all address details for member ID M303.

SELECT *
FROM addressinfo
WHERE memberinfo_member_id = 'M303';

-- 12. Get all X-ray details for cardio ID CID122.

SELECT *
FROM xray
WHERE cardiodiagnosis_cardio_id = 'cid122';

-- 13. Get all symptom details whose cardio ID is CID250 and CID300.

SELECT *
FROM symptom
WHERE cardiodiagnosis_cardio_id IN ('cid250', 'cid300');

-- 14. Get all symptom details for the month of July and year 2019

SELECT *
FROM symptom
WHERE EXTRACT(MONTH FROM date) = 7
  AND EXTRACT(YEAR FROM date) = 2019;

-- 15. Get X-ray details for the member with the last name "Dailley".
SELECT x.*
FROM xray x
JOIN cardiodiagnosis c ON x.cardiodiagnosis_cardio_id = c.cardio_id
JOIN memberinfo m ON c.memberinfo_member_id = m.member_id
WHERE m.lastname = 'dailley';

-- 16. Get wearable device data details for cardio IDs between CID100 and CID200.

SELECT *
FROM wearabledevicedata
WHERE cardiodiagnosis_cardio_id BETWEEN 'cid100' AND 'cid200';

-- 17. Display all cardio diagnosis details where the first name starts with the letter "A".

SELECT c.*
FROM cardiodiagnosis c
JOIN memberinfo m ON c.memberinfo_member_id = m.member_id
WHERE m.firstname LIKE 'a%';

-- 18. Display all cardio diagnosis details where the first name starts with "A" and ends with "A".

SELECT c.*
FROM cardiodiagnosis c
JOIN memberinfo m ON c.memberinfo_member_id = m.member_id
WHERE m.firstname LIKE 'a%a';

-- 19. Get all the members from the MemberInfo table.

SELECT *
FROM memberinfo;

-- 20. Get all the addresses of members.

SELECT *
FROM addressinfo;



