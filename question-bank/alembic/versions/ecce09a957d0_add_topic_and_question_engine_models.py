"""add topic and question engine models

Revision ID: ecce09a957d0
Revises: 
Create Date: 2024-04-27 14:39:28.873990

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = 'ecce09a957d0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('topic',
    sa.Column('title', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('description', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['topic.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_topic_id'), 'topic', ['id'], unique=False)
    op.create_index(op.f('ix_topic_title'), 'topic', ['title'], unique=False)
    op.create_table('content',
    sa.Column('topic_id', sa.Integer(), nullable=True),
    sa.Column('content_text', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['topic_id'], ['topic.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_content_id'), 'content', ['id'], unique=False)
    op.create_index(op.f('ix_content_topic_id'), 'content', ['topic_id'], unique=False)
    op.create_table('questionbank',
    sa.Column('question_text', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.Column('points', sa.Integer(), nullable=False),
    sa.Column('difficulty', sa.Enum('easy', 'medium', 'hard', name='questiondifficultyenum'), nullable=False),
    sa.Column('topic_id', sa.Integer(), nullable=False),
    sa.Column('question_type', sa.Enum('single_select_mcq', 'multiple_select_mcq', name='questiontypeenum'), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['topic_id'], ['topic.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_questionbank_id'), 'questionbank', ['id'], unique=False)
    op.create_table('mcqoption',
    sa.Column('option_text', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('is_correct', sa.Boolean(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['question_id'], ['questionbank.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_mcqoption_id'), 'mcqoption', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_mcqoption_id'), table_name='mcqoption')
    op.drop_table('mcqoption')
    op.drop_index(op.f('ix_questionbank_id'), table_name='questionbank')
    op.drop_table('questionbank')
    op.drop_index(op.f('ix_content_topic_id'), table_name='content')
    op.drop_index(op.f('ix_content_id'), table_name='content')
    op.drop_table('content')
    op.drop_index(op.f('ix_topic_title'), table_name='topic')
    op.drop_index(op.f('ix_topic_id'), table_name='topic')
    op.drop_table('topic')
    # ### end Alembic commands ###