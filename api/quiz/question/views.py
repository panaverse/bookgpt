from fastapi import APIRouter, Depends, Query
from sqlmodel import Session

from api.core.database import get_session
from api.quiz.question.crud import (add_question, read_questions, read_questions_by_type, get_question_by_id, update_question, delete_question,
                                      read_mcq_options, add_mcq_option, delete_mcq_option, update_mcq_option, get_mcq_option_by_id
                                      )

from api.quiz.question.models import QuestionBankCreate, QuestionBankUpdate, QuestionBankRead, MCQOptionCreate, MCQOptionUpdate, MCQOptionRead
from api.core.utils.logger import logger_config

router = APIRouter()

logger = logger_config(__name__)


# ------------------------------------------------------
# ----------------- Question CRUD View -----------------
# ------------------------------------------------------

# Add Question to the Database
@router.post("", response_model=QuestionBankRead)
def call_add_question(question: QuestionBankCreate, db: Session = Depends(get_session)):
    """
    Add a question to the database.

    Args:
        question (QuestionBank): The question to be added.
        db (optional) : Database Dependency Injection.

    Returns:
        QuestionBank: The added question.
    """
    logger.info("%s.create_a_question: %s", __name__, question)
    return add_question(question=question, session=db)

# Get all Questions
@router.get("", response_model=list[QuestionBankRead])
def call_read_questions(offset: int = 0, limit: int = 100, db: Session = Depends(get_session)):
    """
    Get all questions from the database.

    Args:
        offset (int, optional): The offset for pagination. Defaults to 0.
        limit (int, optional): The limit for pagination. Defaults to 100.
       db (optional) : Database Dependency Injection.

    Returns:
        list[QuestionBank]: The list of questions.
    """
    logger.info("%s.get_all_questions", __name__)
    return read_questions(offset=offset, limit=limit, db=db)

# Get all Questions For a Question Type
@router.get("/read/{question_type}", response_model=list[QuestionBankRead])
def call_read_questions_by_type(question_type: str, db: Session = Depends(get_session)):
    """
    Get all questions of a specific question type from the database.

    Args:
        question_type (str): The question type.
       db (optional) : Database Dependency Injection.

    Returns:
        list[QuestionBank]: The list of questions.
    """
    logger.info("%s.get_all_questions_by_type: %s", __name__, question_type)
    return read_questions_by_type(question_type=question_type, db=db)

# Get a Question by ID
@router.get("/{question_id}", response_model=QuestionBankRead)
def call_get_question_by_id(question_id: int, db: Session = Depends(get_session)):
    """
    Get a question by its ID from the database.

    Args:
        question_id (int): The ID of the question.
       db (optional) : Database Dependency Injection.

    Returns:
        QuestionBank: The retrieved question.
    """
    logger.info("%s.get_question_by_id: %s", __name__, question_id)
    return get_question_by_id(id=question_id, db=db)

# Update a Question by ID
@router.patch("/{question_id}", response_model=QuestionBankRead)
def call_update_question(question_id: int, question: QuestionBankUpdate, db: Session = Depends(get_session)):
    """
    Update a question by its ID in the database.

    Args:
        question_id (int): The ID of the question.
        question (QuestionBank): The updated question.
        db (optional) : Database Dependency Injection.

    Returns:
        QuestionBank: The updated question.
    """
    logger.info("%s.update_question: %s", __name__, question)
    return update_question(id=question_id, question=question, db=db)

# Delete a Question by ID
@router.delete("/{question_id}")
def call_delete_question(question_id: int, db: Session = Depends(get_session)):
    """
    Delete a question by its ID from the database.

    Args:
        question_id (int): The ID of the question.
       db (optional) : Database Dependency Injection.

    Returns:
        deletion status.
    """
    logger.info("%s.delete_question: %s", __name__, question_id)
    return delete_question(id=question_id, db=db)


# ------------------------------------------------------
# ----------------- MCQ Question CRUD View -----------------
# ------------------------------------------------------

# Get all MCQ Options
@router.get("/mcq-option/all", response_model=list[MCQOptionRead])
def call_read_mcq_options(db: Session = Depends(get_session)):
    """
    Get all MCQ options from the database.

    Args:
       db (optional) : Database Dependency Injection.

    Returns:
        list[MCQOption]: The list of MCQ options.
    """
    logger.info("%s.get_all_mcq_options", __name__)
    return read_mcq_options(db=db)

# Add MCQ Option to the Database
@router.post("/mcq-option", response_model=MCQOptionRead)
def call_add_mcq_option(mcq_option: MCQOptionCreate, db: Session = Depends(get_session)):
    """
    Add an MCQ option to the database.

    Args:
        mcq_option (MCQOption): The MCQ option to be added.
       db (optional) : Database Dependency Injection.

    Returns:
        MCQOption: The added MCQ option.
    """
    logger.info("%s.add_mcq_option: %s", __name__, mcq_option)
    return add_mcq_option(mcq_option=mcq_option, session=db)

# Get an MCQ Option by ID
@router.get("/mcq-option/{mcq_option_id}", response_model=MCQOptionRead)
def call_get_mcq_option_by_id(mcq_option_id: int, db: Session = Depends(get_session)):
    """
    Get an MCQ option by its ID from the database.

    Args:
        mcq_option_id (int): The ID of the MCQ option.
       db (optional) : Database Dependency Injection.

    Returns:
        MCQOption: The retrieved MCQ option.
    """
    logger.info("%s.get_mcq_option_by_id: %s", __name__, mcq_option_id)
    return get_mcq_option_by_id(id=mcq_option_id, db=db)

# Update an MCQ Option by ID
@router.patch("/mcq-option/{mcq_option_id}", response_model=MCQOptionRead)
def call_update_mcq_option(mcq_option_id: int, mcq_option: MCQOptionUpdate, db: Session = Depends(get_session)):
    """
    Update an MCQ option by its ID in the database.

    Args:
        mcq_option_id (int): The ID of the MCQ option.
        mcq_option (MCQOption): The updated MCQ option.
       db (optional) : Database Dependency Injection.

    Returns:
        MCQOption: The updated MCQ option.
    """
    logger.info("%s.update_mcq_option: %s", __name__, mcq_option)
    return update_mcq_option(id=mcq_option_id, mcq_option=mcq_option, db=db)

# Delete an MCQ Option by ID
@router.delete("/mcq-option/{mcq_option_id}")
def call_delete_mcq_option(mcq_option_id: int, db: Session = Depends(get_session)):
    """
    Delete an MCQ option by its ID from the database.

    Args:
        mcq_option_id (int): The ID of the MCQ option.
       db (optional) : Database Dependency Injection.

    Returns:
        deletion status.
    """
    logger.info("%s.delete_mcq_option: %s", __name__, mcq_option_id)
    return delete_mcq_option(id=mcq_option_id, db=db)
