from django.db import models
from django.utils import timezone

# Create your models here.


# 学生信息表
class StudentInformation(models.Model):
    # 学生学号 主键
    sno = models.CharField(verbose_name="学号，主键", max_length=16, primary_key=True)
    sname = models.CharField(verbose_name="学生姓名", max_length=32)
    ssex = models.IntegerField(verbose_name="学生性别")
    birthdate = models.DateField(verbose_name="出生日期")
    admission = models.DateField(verbose_name="入学时间")
    major_id = models.ForeignKey(verbose_name="专业号", to='MajorInformation', to_field='major_id',
                                 on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(verbose_name="指导教师编号", to='TeacherInformation', to_field='teacher_id',
                                   on_delete=models.CASCADE)


# 指导教师表
class TeacherInformation(models.Model):
    # 教室编号，主键
    teacher_id = models.CharField(verbose_name="指导老师编号", max_length=16, primary_key=True)
    tname = models.CharField(verbose_name="老师姓名", max_length=32)
    tsex = models.IntegerField(verbose_name="教师性别")
    tage = models.IntegerField(verbose_name="教师年龄")
    tsalaries = models.IntegerField(verbose_name="薪水")
    entry_time = models.DateField(verbose_name="入职时间")
    rank = models.CharField(verbose_name="职称", max_length=16)


# 员工信息表
class EmployeeInformation(models.Model):
    employee_id = models.CharField(verbose_name="员工号", max_length=16, primary_key=True)
    ename = models.CharField(verbose_name="员工姓名", max_length=32)
    esex = models.IntegerField(verbose_name="员工性别")
    eage = models.IntegerField(verbose_name="员工年龄")
    esalaries = models.IntegerField(verbose_name="薪水")
    eentry_time = models.DateField(verbose_name="入职时间")
    subject_id = models.ForeignKey(verbose_name="本学期所授课程号", to='SubjectInformation', to_field='subject_id',
                                   on_delete=models.CASCADE)
    department_id = models.ForeignKey(verbose_name="所属部门号", to='DepartmentInformation', to_field='department_id',
                                      on_delete=models.CASCADE)


# 部门信息表
class DepartmentInformation(models.Model):
    department_id = models.CharField(verbose_name="部门号", max_length=16, primary_key=True)
    department_name = models.CharField(verbose_name="部门名称", max_length=32)
    principal = models.ForeignKey(verbose_name="负责人", to='EmployeeInformation', to_field='employee_id',
                                  on_delete=models.CASCADE)


# 专业信息表
class MajorInformation(models.Model):
    major_id = models.CharField(verbose_name="专业号", max_length=16, primary_key=True)
    major_name = models.CharField(verbose_name="专业名", max_length=32)


# 教室信息表
class ClassroomInformation(models.Model):
    classroom_id = models.CharField(verbose_name="教室号", max_length=16, primary_key=True)
    classroom_name = models.CharField(verbose_name="教室名", max_length=32)
    classroom_number = models.IntegerField(verbose_name="容纳人数")


# 课程信息表
class SubjectInformation(models.Model):
    subject_id = models.CharField(verbose_name="课程号", max_length=16, primary_key=True)
    subject_name = models.CharField(verbose_name="课程名称", max_length=32)
    start_time = models.DateField(verbose_name="开始时间")
    end_time = models.DateField(verbose_name="结束时间")
    classroom_id = models.ForeignKey(verbose_name="教室号", to='ClassroomInformation', to_field='classroom_id',
                                     on_delete=models.CASCADE)


# 专业-课程表
class MajorSubject(models.Model):
    major_id = models.ForeignKey(verbose_name="专业号", to='MajorInformation', to_field='major_id',
                                 on_delete=models.CASCADE)
    subject_id = models.ForeignKey(verbose_name="课程号", to='SubjectInformation', to_field='subject_id',
                                   on_delete=models.CASCADE)


# 账号表
class Accounts(models.Model):
    user_id = models.CharField(verbose_name="账户", max_length=16)
    user_password = models.CharField(verbose_name="密码", max_length=32)
    identity = models.CharField(verbose_name="身份", max_length=16)


# 学生—课程表
class StudentSubject(models.Model):
    student_id = models.ForeignKey(verbose_name="学生号", to='StudentInformation', to_field="sno",
                                   on_delete=models.Model)
    subject_id = models.ForeignKey(verbose_name="课程号", to='SubjectInformation', to_field='subject_id',
                                   on_delete=models.CASCADE)
    times = models.IntegerField(verbose_name="考试次数", default=3)
    score = models.IntegerField(verbose_name="分数")