"""test

Revision ID: f0386b49d1d8
Revises: c6d4b285b2e1
Create Date: 2024-03-16 23:55:56.284352

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'f0386b49d1d8'
down_revision: Union[str, None] = 'c6d4b285b2e1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_task_audit_action', table_name='task_audit')
    op.drop_index('ix_task_audit_id', table_name='task_audit')
    op.drop_table('task_audit')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('task_audit',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('task_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('action', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('timestamp', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('performed_by', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['performed_by'], ['users.id'], name='task_audit_performed_by_fkey'),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], name='task_audit_task_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='task_audit_pkey')
    )
    op.create_index('ix_task_audit_id', 'task_audit', ['id'], unique=False)
    op.create_index('ix_task_audit_action', 'task_audit', ['action'], unique=False)
    # ### end Alembic commands ###
