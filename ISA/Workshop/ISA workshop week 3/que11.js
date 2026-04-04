function getBestStudent(students) {
    let bestStudent = "";
    let highestAvg = 0;
    for (let student in students) {
        let grades = students[student];
        let sum = 0;
        for (let i = 0; i < grades.length; i++) {
            sum += grades[i];
        }
        let avg = sum / grades.length;

        if (avg > highestAvg) {
            highestAvg = avg;
            bestStudent = student;
        }
    }
    console.log(bestStudent);
}
const studentGrades = {
    John: [100, 90, 80],
    Bob: [100, 70, 80],
    Alice: [95, 85, 90]
};
getBestStudent(studentGrades); 