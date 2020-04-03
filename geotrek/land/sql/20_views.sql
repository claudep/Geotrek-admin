DROP VIEW IF EXISTS f_v_nature;
DROP VIEW IF EXISTS v_physicals;
DROP VIEW IF EXISTS f_v_foncier;
DROP VIEW IF EXISTS v_lands;
DROP VIEW IF EXISTS f_v_competence;
DROP VIEW IF EXISTS v_competences;
DROP VIEW IF EXISTS f_v_gestion_signaletique;
DROP VIEW IF EXISTS v_signagemanagements;
DROP VIEW IF EXISTS f_v_gestion_travaux;
DROP VIEW IF EXISTS v_workmanagements;

CREATE OR REPLACE VIEW {# geotrek.land #}.v_physicals AS (
	SELECT e.*, b.name, b.structure_id
	FROM core_topology AS e, land_physicaledge AS f, land_physicaltype AS b
	WHERE f.topo_object_id = e.id AND f.physical_type_id = b.id
	AND deleted = FALSE
);

CREATE OR REPLACE VIEW {# geotrek.land #}.v_lands AS (
	SELECT e.*, b.structure_id, b.name, b.right_of_way
	FROM core_topology AS e, land_landedge AS f, land_landtype AS b
	WHERE f.topo_object_id = e.id AND f.land_type_id = b.id
	AND deleted = FALSE
);

CREATE OR REPLACE VIEW {# geotrek.land #}.v_competences AS (
	SELECT e.*, b.structure_id, b.organism
	FROM core_topology AS e, land_competenceedge AS f, common_organism AS b
	WHERE f.topo_object_id = e.id AND f.organization_id = b.id
	AND deleted = FALSE
);

CREATE OR REPLACE VIEW {# geotrek.land #}.v_signagemanagements AS (
	SELECT e.*, b.structure_id, b.organism
	FROM core_topology AS e, land_signagemanagementedge AS f, common_organism AS b
	WHERE f.topo_object_id = e.id AND f.organization_id = b.id
	AND deleted = FALSE
);

CREATE OR REPLACE VIEW {# geotrek.land #}.v_workmanagements AS (
	SELECT e.*, b.structure_id, b.organism
	FROM core_topology AS e, land_workmanagementedge AS f, common_organism AS b
	WHERE f.topo_object_id = e.id AND f.organization_id = b.id
	AND deleted = FALSE
);