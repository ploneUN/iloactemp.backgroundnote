from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from zope.interface import invariant, Invalid

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.multilingualbehavior.directives import languageindependent

from collective import dexteritytextindexer


from iloactemp.backgroundnote import MessageFactory as _


# Interface class; used to define content-type schema.

class INote(form.Schema, IImageScaleTraversable):
    """
    ACT/EMP Background Note
    """
    dexteritytextindexer.searchable('title')
    title = schema.TextLine(title=u'Country',
                    description=u'Name of country for this background '
                    'note.')

    dexteritytextindexer.searchable('description')
    description = schema.Text(
            title=u'Summary',
            description=u'Used in item listings and search results.',
            default=u'ACT/EMP Background Note & Country Strategy on ')

    organization_information = RichText(
            title=u'Basic organizational information',
            required=False,
            default=u'''
            <p>
            <em>Foundation Date:</em> 
            </p>

            <p>
            <strong>President</strong> : <br/>
            <strong>Secretary General</strong> : <br />
            <strong>Executive Director</strong> : <br />
            </p>

            <p>
            <strong>Located</strong> on: <br />
            <strong>Phone</strong> : <br />
            <strong>Fax</strong> : <br />
            <strong>E-mail</strong> : <br />
            <strong>Website</strong> : <br />
            </p>

            '''
            )

    organization_comment = schema.Text(
            title=u'ACT/EMP Comment',
            required=False)

    regulation_source = RichText(
            title = u'Source of regulation',
            required=False)

    regulation_comment = schema.Text(
            title=u'ACT/EMP Comment',
            required=False
            )

    membership = RichText(
            title=u'Membership',
            required=False
            )

    membership_comment = schema.Text(
            title=u'ACT/EMP Comment',
            required=False,
            )

    structure = RichText(
            title=u'Structure',
            required=False
            )

    structure_comment = schema.Text(
            title=u'ACT/EMP Comment',
            required=False,
            )


    involvement_ilo = RichText(
            title=u'Involvement in the ILO governance and supervisory '
            'structures',
            required=False,
            )

    involvement_ilo_comment = schema.Text(
            title=u'ACT/EMP Comment',
            required=False,
            )

    involvement_other = RichText(
            title=u'Involvement in other international bodies',
            required=False,
            )

    involvement_other_comment = schema.Text(
            title=u'ACT/EMP Comment',
            required=False,
            )

    overview_country = RichText(
            title=u'Overview of country context',
            required=False,
            default=u'''
            <u>Overall picture according to international indices</u>
            
            <p>

            <table class="listing">
            <tr>
                <th>Doing Business</th>
                <td>Rank: </td>
            </tr>
            <tr>
                <th>IMD world competiveness</th>
                <td>Rank: </td>
            </tr>
            <tr>
                <th>WEF Competitiveness</th>
                <td>Rank: </td>
            </tr>
            <tr>
                <th>WEF - Quality of Education System</th>
                <td>Rank: </td>
            </tr>
            <tr>
                <th>Deloiite Global CEO Survey: <br />
                manufacturing competitiveness index rankings
                </th>
                <td>Rank: </td>
            </tr>
            <tr>
                <th>UNDP Human Development Index</th>
                <td>Rank: </td>
            </tr>
            <tr>
                <th>UN HDI - Education</th>
                <td>Rank: </td>
            </tr>
            <tr>
                <th>Gini Coefficient (UN )</th>
                <td>Rank: </td>
            </tr>
            <tr>
                <th>GDP per capita</th>
                <td>Rank: </td>
            </tr>
            <tr>
                <th>Extent of staff training (WEF)</th>
                <td>Rank: </td>
            </tr>
            <tr>
                <th>Public spending on Education % GDP</th>
                <td>Rank: </td>
            </tr>
            <tr>
                <th>Pearson ranking of education systems</th>
                <td>Rank: </td>
            </tr>
            <tr>
                <th>Tax revenue as % of GDP World Bank</th>
                <td> % </td>
            </tr>
            <tr>
                <th>New business density (World Bank Surveys)</th>
                <td> </td>
            </tr>
            <tr>
                <th>Government t effectivness (WB)</th>
                <td>Rank: (100 is best)</td>
            </tr>
            <tr>
                <th>Control of corruption (WB)</th>
                <td>Rank: (0 is worst)</td>
            </tr>
            <tr>
                <th>Regulatory quality index</th>
                <td>Rank: (100 is best)</td>
            </tr>
            <tr>
                <th>Rule of Law (WB)</th>
                <td>Rank: (0 is worst)</td>
            </tr>
            <tr>
                <th>Political Stability</th>
                <td>Rank: (100 is best)</td>
            </tr>
            <tr>
                <th>Democracy/Voice (WB 2011)</th>
                <td>Rank: (0 is worst)</td>
            </tr>
            </table>
            '''
            )

    overview_country_comment = schema.Text(
            title=u'ACT/EMP Comment',
            required=False,
            )

    overview_business = RichText(
            title=u'Overview of the overall national business agenda',
            required=False,
            )

    overview_business_comment = schema.Text(
            title=u'ACT/EMP Comment',
            required=False,
            )

    business_representatives = RichText(
            title=u'Main Business representatives',
            required=False,
            )

    key_policies = RichText(
            title=u'Key policy priorities of the EO',
            required=False,
            )

    key_policies_comment = schema.Text(
            title=u'ACT/EMP Comment',
            required=False,
            )

    policy_dialogue = RichText(
            title=u'Policy dialogue modalities',
            required=False,
            )

    policy_dialogue_comment = schema.Text(
            title=u'ACT/EMP Comment',
            required=False,
            )

    key_documents = RichText(
            title=u'Key policy documents / Sources of information '
                   'and documentation',
            required=False,
            )
   
    attachment_1 = NamedBlobFile(
            title=u'File Attachment 1',
            required=False,
            )

    attachment_2 = NamedBlobFile(
            title=u'File Attachment 2',
            required=False,
            )

    attachment_3 = NamedBlobFile(
            title=u'File Attachment 3',
            required=False,
            )


    attachment_4 = NamedBlobFile(
            title=u'File Attachment 4',
            required=False,
            )

    attachment_5 = NamedBlobFile(
            title=u'File Attachment 5',
            required=False,
            )

    #Organizational Analysis

    vision = RichText(
            title=u'Visual, objectives and mission statement',
            required=False,
            )

    vision_comment = schema.Text(
            title=u'ACT/EMP Comment',
            required=False,
            )

    assessment_membership = RichText(
            title=u'Assessment of membership',
            required=False,
            )

    assessment_membership_comment = schema.Text(
            title=u'ACT/EMP Comment',
            required=False,
            )

    direct_services = RichText(
            title=u'Direct services',
            required=False,
            )

    direct_services_comment = schema.Text(
            title=u'ACT/EMP Comment',
            required=False,
            )

    advocacy_services = RichText(
            title=u'Advocacy Services',
            required=False,
            )
    advocacy_services_comment = schema.Text(
            title=u'ACT/EMP Comment',
            required=False,
            )

    income = RichText(
            title=u'Income',
            required=False,
            )

    income_comment= schema.Text(
            title=u'ACT/EMP Comment',
            required=False,
            )

    relations = RichText(
            title=u'Relations with the government and trade unions',
            required=False,
            )

    relations_comment = schema.Text(
            title=u'ACT/EMP Comment',
            required=False,
            )


    #D. Relations with ILO, UN, Multilateral and bilateral Development

    engagement_dwcp = RichText(
            title=u'Engagement in the DWCP',
            required=False,
            )
    engagement_dwcp_comment = schema.Text(
            title=u'ACT/EMP Comment',
            required=False,
            )

    ilo_policy = RichText(
            title=u'Views on ILO policy in a particular field',
            required=False,
            )
    ilo_policy_comment = schema.Text(
            title=u'ACT/EMP Comment',
            required=False,
            )

    results_ilo_support = RichText(
            title=u'Major results achieved with the ILO support in '
            'the last biennium',
            required=False,
            )
    results_ilo_support_comment = schema.Text(
            title=u'ACT/EMP Comment',
            required=False,
            )
    ilo_projects = RichText(
            title=u'ILO project the EO is involved in',
            required=False,
            )
    ilo_projects_comment = schema.Text(
            title=u'ACT/EMP Comment',
            required=False,
            )

    summary_assistance = RichText(
            title=u'Summary of any other international '
            'assistance/funding provided by donor '
            'governments or bilateral development cooperation '
            'agencies',
            required=False,
            )
    summary_assistance_comment = schema.Text(
            title=u'ACT/EMP Comment',
            required=False,
            )

    recent_activities = RichText(
            title=u'Recent ACT/EMP activities',
            required=False,
            )
    recent_activities_comment = schema.Text(
            title=u'ACT/EMP Comment',
            required=False,
            )

    ITC_training = RichText(
            title=u'Involvement in ILO ITC training',
            required=False,
            )
    ITC_training_comment = schema.Text(
            title=u'ACT/EMP Comment',
            required=False,
            )

    UNDAF = RichText(
            title=u'Involvement in the UNDAF development and '
            'implementation',
            required=False,
            )
    UNDAF_comment = schema.Text(
            title=u'ACT/EMP Comment',
            required=False,
            )

    # E. ACTEMP Strategy

    org_needs = RichText(
            title=u'Organizational needs analysis / baseline situation',
            required=False,
            )
    org_needs_comment = schema.Text(
            title = u'ACT/EMP Comment',
            required=False,
            )

    major_issues = RichText(
            title=u'Current major issues or objectives that need '
            'to be addressed in the EO and how do these issues '
            'or objectives align with the EO\'s '
            'organizational/strategic plans',
            required=False,
            )
    major_issues_comment = schema.Text(
            title=u'ACT/EMP Commment',
            required=False,
            )

    intended_results = RichText(
            title=u'Results intended to be achieved by ACTEMP',
            required=False,
            )

    intended_results_comment = schema.Text(
            title=u'ACT/EMP Comment',
            required=False,
            )


