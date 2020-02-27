# This module is automatically generated by autogen.sh. DO NOT EDIT.

from . import _AWS


class _Database(_AWS):
    _type = "database"
    _icon_dir = "resources/aws/database"


class Aurora(_Database):
    _icon = "aurora.png"


class DatabaseMigrationService(_Database):
    _icon = "database-migration-service.png"


class Database(_Database):
    _icon = "database.png"


class DocumentdbMongodbCompatibility(_Database):
    _icon = "documentdb-mongodb-compatibility.png"


class Dynamodb(_Database):
    _icon = "dynamodb.png"


class Elasticache(_Database):
    _icon = "elasticache.png"


class Neptune(_Database):
    _icon = "neptune.png"


class QuantumLedgerDatabaseQldb(_Database):
    _icon = "quantum-ledger-database-qldb.png"


class RDSOnVmware(_Database):
    _icon = "rds-on-vmware.png"


class RDS(_Database):
    _icon = "rds.png"


class Redshift(_Database):
    _icon = "redshift.png"


class Timestream(_Database):
    _icon = "timestream.png"


# Aliases

DMS = DatabaseMigrationService
DocumentDB = DocumentdbMongodbCompatibility
DB = Database
DDB = Dynamodb
ElastiCache = Elasticache
QLDB = QuantumLedgerDatabaseQldb
