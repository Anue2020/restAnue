package anue.web.model;

import java.util.Objects;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonCreator;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import org.openapitools.jackson.nullable.JsonNullable;
import javax.validation.Valid;
import javax.validation.constraints.*;

/**
 * Post-Response bei erfolgreicher ...
 */
@ApiModel(description = "Post-Response bei erfolgreicher ...")
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.SpringCodegen", date = "2021-02-13T14:21:22.739836+01:00[Europe/Berlin]")

public class PostResponseDto   {
  @JsonProperty("irgendwas_Id")
  private String irgendwasId;

  public PostResponseDto irgendwasId(String irgendwasId) {
    this.irgendwasId = irgendwasId;
    return this;
  }

  /**
   * asdasdasd
   * @return irgendwasId
  */
  @ApiModelProperty(example = "rudolfrudio", value = "asdasdasd")


  public String getIrgendwasId() {
    return irgendwasId;
  }

  public void setIrgendwasId(String irgendwasId) {
    this.irgendwasId = irgendwasId;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PostResponseDto postResponse = (PostResponseDto) o;
    return Objects.equals(this.irgendwasId, postResponse.irgendwasId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(irgendwasId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PostResponseDto {\n");
    
    sb.append("    irgendwasId: ").append(toIndentedString(irgendwasId)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }
}

