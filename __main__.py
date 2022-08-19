from pdp_graphql import PDPGraphQL

pdp = PDPGraphQL("a7e5d1e9-4d50-454e-9fd0-2a95263e06da", "3sL8Q~VAtiwAkfPmGlRlJ2~QZH3rJOk.-.XWiaf1")

response = pdp.query(
    """{
  assets(
    identifiers: [
      "urn:srf:video:ca14da25-614e-4614-b08d-bba715b33205"
      "urn:srf:article:20097176"
    ]
  ) {
    identifier
    hasProvenance
    hasType
    ... on Item {
      duration
      dateModified
      hasProvenance
      title
      hasProductionType
      hasProducer
      hasUsageRestrictions
      hasParentEditorialObject {
          dateBroadcast
          dateProduced
          dateModified
      }
    }
    ... on Document {
      title
      dateReleased
      commentsAllowed
      isLongForm
      kicker
      abstract
      hasPublisher
      hasRelatedTextLine
      hasContributor {
          hasType
          ... on Person {
              hasRole
              givenName
              familyName
              agentName
          }
          ... on Department {
              agentName
          }
          ... on Team {
              agentName
          }
      }
      hasRelatedEditorialObject {
        identifier
        title
        duration
      }
      hasGenre {
        identifier
        prefLabel
      }
    }
  }
}
"""
)
# Prints the response of the pdp api
print(response)