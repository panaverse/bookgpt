from fastapi import Depends, HTTPException, status
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.database.db import get_session
from services.quiz.university.models import (
    UniversityCreate, UniversityRead, UniversityUpdate, University,
    ProgramCreate, ProgramRead, ProgramUpdate, Program,
    CourseCreate, CourseRead, CourseUpdate, Course
    )

# function to create a university, program, and course
async def create_university(university: UniversityCreate, db: AsyncSession = Depends(get_session)):
    uni_to_db = University.model_validate(university)
    db.add(uni_to_db)
    await db.commit()
    db.refresh(uni_to_db)
    return uni_to_db

async def create_program(program: ProgramCreate, db: AsyncSession = Depends(get_session)):
    program_to_db = Program.model_validate(program)
    db.add(program_to_db)
    await db.commit()
    db.refresh(program_to_db)
    return program_to_db

async def create_course(course: CourseCreate, db: AsyncSession = Depends(get_session)):
    course_to_db = Course.model_validate(course)
    db.add(course_to_db)
    await db.commit()
    db.refresh(course_to_db)
    return course_to_db

# function to read universities, programs, and courses
async def read_universities(offset: int = 0, limit: int = 10, db: AsyncSession = Depends(get_session)):
    async with db as session:
        result = await session.execute(select(University).offset(offset).limit(limit))
        universities = result.scalars().all()
        return universities

async def read_programs(offset: int = 0, limit: int = 10, db: AsyncSession = Depends(get_session)):
    programs = await db.exec(select(Program).offset(offset).limit(limit)).all()
    return programs

async def read_courses(offset: int = 0, limit: int = 10, db: AsyncSession = Depends(get_session)):
    courses = await db.exec(select(Course).offset(offset).limit(limit)).all()
    return courses

# function to read a university, program, and course
async def read_university(university_id: int, db: AsyncSession = Depends(get_session)):
    university = db.get(University, university_id)
    if not University:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"University not found with id: {university_id}",
        )
    return university

async def read_program(program_id: int, db: AsyncSession = Depends(get_session)):
    program = db.get(Program, program_id)
    if not program:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Program not found with id: {program_id}",
        )
    return program

async def read_course(course_id: int, db: AsyncSession = Depends(get_session)):
    course = db.get(Course, course_id)
    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course not found with id: {course_id}",
        )
    return course

# function to update a university, program, and course
async def update_university(university_id: int, university: UniversityUpdate, db: AsyncSession = Depends(get_session)):
    university_to_update = db.get(University, university_id)
    if not university_to_update:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"University not found with id: {university_id}",
        )
    
    db.add(university_to_update)
    await db.commit()
    db.refresh(university_to_update)
    return university_to_update

async def update_program(program_id: int, program: ProgramUpdate, db: AsyncSession = Depends(get_session)):
    program_to_update = db.get(Program, program_id)
    if not program_to_update:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Program not found with id: {program_id}",
        )
    
    db.add(program_to_update)
    await db.commit()
    db.refresh(program_to_update)
    return program_to_update

async def update_course(course_id: int, course: CourseUpdate, db: AsyncSession = Depends(get_session)):
    course_to_update = db.get(Course, course_id)
    if not course_to_update:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course not found with id: {course_id}",
        )
    
    db.add(course_to_update)
    await db.commit()
    db.refresh(course_to_update)
    return course_to_update

# function to delete a university, program, and course
async def delete_university(university_id: int, db: AsyncSession = Depends(get_session)):
    university = db.get(University, university_id)
    if not university:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"University not found with id: {university_id}",
        )

    db.delete(university)
    await db.commit()
    return {"ok": True}

async def delete_program(program_id: int, db: AsyncSession = Depends(get_session)):
    program = db.get(Program, program_id)
    if not program:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Program not found with id: {program_id}",
        )

    db.delete(program)
    await db.commit()
    return {"ok": True}

async def delete_course(course_id: int, db: AsyncSession = Depends(get_session)):
    course = db.get(Course, course_id)
    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course not found with id: {course_id}",
        )

    db.delete(course)
    await db.commit()
    return {"ok": True}