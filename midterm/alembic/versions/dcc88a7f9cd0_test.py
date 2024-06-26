"""test

Revision ID: dcc88a7f9cd0
Revises: f0386b49d1d8
Create Date: 2024-03-16 23:58:13.497558

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dcc88a7f9cd0'
down_revision: Union[str, None] = 'f0386b49d1d8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('task_audit',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('task_id', sa.Integer(), nullable=True),
    sa.Column('action', sa.String(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('performed_by', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['performed_by'], ['users.id'], ),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_task_audit_action'), 'task_audit', ['action'], unique=False)
    op.create_index(op.f('ix_task_audit_id'), 'task_audit', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_task_audit_id'), table_name='task_audit')
    op.drop_index(op.f('ix_task_audit_action'), table_name='task_audit')
    op.drop_table('task_audit')
    # ### end Alembic commands ###
