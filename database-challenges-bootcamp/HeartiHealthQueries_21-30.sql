-- 21. Get a list of wearable device information.

SELECT *
FROM wearabledevicedata;

-- 22. Get a list of all the blood tests done.

SELECT *
FROM bloodtest;

-- 23. Get a list of members who are aged greater than 50.
SELECT *
FROM memberinfo
WHERE age > 50;

-- 24. Get a list of addresses for the city 'Flora'.

SELECT *
FROM addressinfo
WHERE city = 'Flora';

-- 25. Get a list of all unique states

SELECT DISTINCT state
FROM addressinfo;

-- 26. Get the total number of members in the database.

SELECT COUNT(*) AS total_members
FROM memberinfo;

-- 27. Get the total number of blood tests done.

SELECT COUNT(*) AS total_blood_tests
FROM bloodtest;

-- 28. Get the average cholesterol level for members

SELECT AVG(serumcholesterol) AS avg_cholesterol
FROM bloodtest;

-- 29. Get the maximum peak value in symptoms.

SELECT MAX(oldpeak) AS max_peak
FROM symptom;

-- 30. Get the list of tests done between January 1, 2015, and January 31, 2019.

SELECT *
FROM bloodtest
WHERE DATE(date) BETWEEN '2015-01-01' AND '2019-01-31';
