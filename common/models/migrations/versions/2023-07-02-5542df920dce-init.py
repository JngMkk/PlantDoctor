"""init

Revision ID: 5542df920dce
Revises: 
Create Date: 2023-07-02 03:53:40.457275

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5542df920dce'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('humidEnv',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sqlmodel.sql.sqltypes.AutoString(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('humidSumm',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sqlmodel.sql.sqltypes.AutoString(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lightLocation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sqlmodel.sql.sqltypes.AutoString(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lightSumm',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sqlmodel.sql.sqltypes.AutoString(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('plantDiseases',
    sa.Column('symptom', mysql.TEXT(), nullable=True),
    sa.Column('env', mysql.TEXT(), nullable=True),
    sa.Column('precaution', mysql.TEXT(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('koNm', sqlmodel.sql.sqltypes.AutoString(length=10), nullable=False),
    sa.Column('enNm', sqlmodel.sql.sqltypes.AutoString(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('plantManagement',
    sa.Column('createdAt', sa.DateTime(), nullable=True),
    sa.Column('updatedAt', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.Column('plantId', sa.Integer(), nullable=False),
    sa.Column('image', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=True),
    sa.Column('nickName', sqlmodel.sql.sqltypes.AutoString(length=20), nullable=False),
    sa.Column('meetDate', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_plantManagement_plantId'), 'plantManagement', ['plantId'], unique=False)
    op.create_index(op.f('ix_plantManagement_userId'), 'plantManagement', ['userId'], unique=False)
    op.create_table('plantRequest',
    sa.Column('createdAt', sa.DateTime(), nullable=True),
    sa.Column('updatedAt', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.Column('plantName', sqlmodel.sql.sqltypes.AutoString(length=64), nullable=False),
    sa.Column('isChecked', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('plants',
    sa.Column('waterDetail', mysql.TEXT(), nullable=True),
    sa.Column('lightDetail', mysql.TEXT(), nullable=True),
    sa.Column('humidDetail', mysql.TEXT(), nullable=True),
    sa.Column('tempDetail', mysql.TEXT(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
    sa.Column('koNm', sqlmodel.sql.sqltypes.AutoString(length=16), nullable=False),
    sa.Column('enNm', sqlmodel.sql.sqltypes.AutoString(length=64), nullable=False),
    sa.Column('summ', sqlmodel.sql.sqltypes.AutoString(length=128), nullable=False),
    sa.Column('waterCycleId', sa.Integer(), nullable=False),
    sa.Column('waterMethodId', sa.Integer(), nullable=False),
    sa.Column('waterMethodDetailId', sa.Integer(), nullable=False),
    sa.Column('lightLocationId', sa.Integer(), nullable=False),
    sa.Column('lightSummId', sa.Integer(), nullable=False),
    sa.Column('humidEnvId', sa.Integer(), nullable=False),
    sa.Column('humidSummId', sa.Integer(), nullable=False),
    sa.Column('tempEnvId', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tempEnv',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sqlmodel.sql.sqltypes.AutoString(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('createdAt', sa.DateTime(), nullable=True),
    sa.Column('updatedAt', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sqlmodel.sql.sqltypes.AutoString(length=100), nullable=False),
    sa.Column('pw', sqlmodel.sql.sqltypes.AutoString(length=60), nullable=False),
    sa.Column('isAdmin', sa.Boolean(), nullable=True),
    sa.Column('isActive', sa.Boolean(), nullable=True),
    sa.Column('lastLogin', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=False)
    op.create_index(op.f('ix_users_pw'), 'users', ['pw'], unique=False)
    op.create_table('waterCycle',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sqlmodel.sql.sqltypes.AutoString(length=8), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('waterMethod',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sqlmodel.sql.sqltypes.AutoString(length=40), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('waterMethodDetail',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sqlmodel.sql.sqltypes.AutoString(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('waterMethodDetail')
    op.drop_table('waterMethod')
    op.drop_table('waterCycle')
    op.drop_index(op.f('ix_users_pw'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_table('tempEnv')
    op.drop_table('plants')
    op.drop_table('plantRequest')
    op.drop_index(op.f('ix_plantManagement_userId'), table_name='plantManagement')
    op.drop_index(op.f('ix_plantManagement_plantId'), table_name='plantManagement')
    op.drop_table('plantManagement')
    op.drop_table('plantDiseases')
    op.drop_table('lightSumm')
    op.drop_table('lightLocation')
    op.drop_table('humidSumm')
    op.drop_table('humidEnv')
    # ### end Alembic commands ###